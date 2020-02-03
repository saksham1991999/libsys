from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.db.models import Q

from . import models, forms

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict=None):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def CurrentAffairsView(request):
    all_categories = models.current_affair_categories.objects.all()
    all_current_affairs = models.current_affair.objects.order_by('-postedon')
    latest_current_affairs = all_current_affairs[:5]
    search_term = ''

    if 'category' in request.GET:
        selected_category_title = request.GET.get('category')
        all_current_affairs = all_current_affairs.filter(category__title=selected_category_title)

    if 'search' in request.GET:
        search_term = request.GET['search']
        all_current_affairs = all_current_affairs.filter(Q(title__icontains = search_term)| Q(description__icontains=search_term))

    paginator = Paginator(all_current_affairs, 5)

    page = request.GET.get('page')
    all_current_affairs = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {
        'categories': all_categories,
        'currentaffairs': all_current_affairs,
        'allcurrentaffairs': latest_current_affairs,
        'params': params,
        'search_term': search_term
    }
    return render(request, 'currentaffairs.html', context)


def CurrentAffairView(request, id):
    current_affair = get_object_or_404(models.current_affair, id = id)
    comments = models.comment.objects.filter(current_affair=current_affair)
    all_categories = models.current_affair_categories.objects.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.CommentForm(request.POST)
            if form.is_valid():
                new_comment = models.comment()
                new_comment.comment_text = form.cleaned_data.get('comment_text')
                new_comment.current_affair = current_affair
                new_comment.date = date.today()
                new_comment.user = request.user
                new_comment.name = form.cleaned_data.get('name')
                new_comment.save()
                messages.success(
                    request,
                    'Comment Added Successfully',
                    extra_tags='alert alert-success alert-dismissible fade show'
                )
                return redirect('exams:currentaffair', id)
        else:
            messages.success(
                request,
                'Login to add a comment',
                extra_tags='alert alert-alert alert-dismissible fade show'
            )
            return redirect('exams:currentaffair', id)
    else:
        commentform = forms.CommentForm()
        context = {
            'commentform': commentform,
            'currentaffair': current_affair,
            'comments': comments,
            'categories': all_categories,
        }
        return render(request, 'currentaffair.html', context)


def PreviousYearQAView(request):
    files = models.previous_year.objects.all().order_by('year')
    search_term = ''

    # if 'category' in request.GET:
    #     selected_category_title = request.GET.get('category')
    #     all_current_affairs = all_current_affairs.filter(category__title=selected_category_title)
    #
    # if 'search' in request.GET:
    #     search_term = request.GET['search']
    #     all_current_affairs = all_current_affairs.filter(Q(title__icontains = search_term)| Q(library_description__icontains=search_term))

    paginator = Paginator(files, 10)

    page = request.GET.get('page')
    files = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {
        'files': files,
        'params': params,
        'search_term': search_term
    }
    return render(request, 'previousyearqa.html', context)


def download(request, id, no):
    test = get_object_or_404(models.previous_year, id=id)
    if no == 1:
        # pdf = test.questions.url
        pdf = open('C:/Users/hp/Desktop/Django Projects/libsys/media_root/previous_years/softeng.pdf', 'r', encoding="utf-8",errors='ignore')
    else:
        pdf = test.answers
    print(pdf)
    return HttpResponse(pdf.read(), content_type='application/pdf')

def testView(request):
    context = {}
    return render(request, 'MCQ/test.html', context)