from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date

from . import models, forms


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
        all_current_affairs = all_current_affairs.filter(Q(title__icontains = search_term)| Q(library_description__icontains=search_term))

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
