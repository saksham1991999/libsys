from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from . import models, forms, serializers
from blog.models import post


def HomeView(request):
    libraries = models.library.objects.all()[:6]
    blogposts = post.objects.all()[:3]
    testimonials = models.testimonial.objects.all()[:3]

    context = {
        'libraries': libraries,
        'blogposts':blogposts,
        'testimonials':testimonials,
    }
    return render(request, 'index.html', context)

def LibrariesView(request):
    allLibraries = models.library.objects.all()
    amenities = models.ammenities.objects.all()
    search_term = ''
    city = ''

    for i in range(10):
        print()
    print(request.GET)

    if 'city' in request.GET:
        city = request.GET['city']
        allLibraries = allLibraries.filter(city__icontains=city)

    if 'seats' in request.GET:
        seats = request.GET['seats']
        allLibraries = allLibraries.filter(no_of_seats=seats)

    if 'search' in request.GET:
        search_term = request.GET['search']
        allLibraries = allLibraries.filter(name__icontains=search_term)

    paginator = Paginator(allLibraries, 25)
    page = request.GET.get('page')
    allLibraries = paginator.get_page(page)

    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()
    context = {
        'libraries': allLibraries,
        'params': params,
        'search_term': search_term,
        'amenities': amenities,
        'city': city,
    }
    return render(request, 'libraries.html', context)

def ContactView(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print('Form saved Successfully')
            messages.success(
                request,
                'Message sent Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        else:
            print(form.errors)
            print('form not valid')
        return redirect('core:contact')
    else:
        form = forms.ContactForm()
        context = {
            'contactform': form,
        }
        return render(request, 'contact.html', context)

def LibraryView(request, id):
    library = get_object_or_404(models.library, id = id)
    library.views = int(library.views + 1)
    library.save()
    images = models.library_images.objects.filter(library=library)
    ammenities = library.ammenities.all()
    payment_methods = library.payment_methods.all()

    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Enquiry sent Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('core:library', id)
        else:
            print(form.errors)
            print(form.errors)
            print(form.errors)
            print(form.errors)
            print(form.errors)
            print(form.errors)
            return redirect('core:library', id)

    else:
        enquiryform = forms.EnquiryForm()
        context = {
            'library': library,
            'images': images,
            'ammenties': ammenities,
            'payment_methods':payment_methods,
            'enquiryform': enquiryform,
        }
        return render(request, 'library.html', context)

def BugReportView(request):
    if request.method == 'POST':
        form = forms.BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Enquiry sent Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('core:reportbug')
        else:
            print(form.errors)
            return redirect('core:reportbug')

    else:
        bugreportform = forms.BugReportForm()
        context = {
            'bugreportform': bugreportform,
        }
        return render(request, 'reportbug.html', context)

def TestimonialsView(request):
    if request.method == 'POST':
        form = forms.TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Enquiry sent Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
            return redirect('core:testimonial')
        else:
            print(form.errors)
            return redirect('core:testimonial')
    else:
        testimonialform = forms.TestimonialForm()
        context = {
            'testimonialform': testimonialform,
        }
        return render(request, 'testimonialform.html', context)

def FAQView(request):
    faqs = models.faq.objects.all()
    context = {
        'faqs':faqs,
    }
    return render(request, 'faq.html', context)

def FAQDetailView(request, id):
    faq = get_object_or_404(models.faq, id=id)
    context = {
        'faq':faq,
    }
    return render(request, 'faqdetail.html', context)

@login_required
def UserProfileView(request):
    if request.method == "POST":
        print(request)
        user = models.User(email=request.user.email)
        form = forms.UserProfileForm(request.POST, instance=request.user)
        # fname = form[]
        print('fsddddddddddddddddddddddddddddddddddfdsfdsfdsfdsfdsfds')
        print(form)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Changes Saved Successfully',
                extra_tags='alert alert-success alert-dismissible fade show'
            )
        return redirect('core:userprofile')
    else:
        form = forms.UserProfileForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'dashboard/userprofile.html', context)

@login_required
def myLibraries(request):
    libraries = models.library.objects.filter(owner = request.user)
    context = {
        'libraries': libraries,
    }
    return render(request, 'dashboard/mylibraries.html', context)

@login_required
def editLibrary(request, id):
    library = get_object_or_404(models.library, id=id)
    if library.owner == request.user:
        if request.method == 'POST':
            form = forms.LibraryForm(request.POST, instance=library)
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    'Property Details Saved Successfully',
                    extra_tags='alert alert-success alert-dismissible fade show'
                )
                return redirect('core:mylibraries')
            else:
                return redirect('core:editlibrary', id)
        else:
            form = forms.LibraryForm(instance=library)
            context = {
                'form': form,
            }
            return render(request, 'dashboard/addlibrary.html', context)
    else:
        messages.success(
            request,
            'You are not allowed to edit the Property Details',
            extra_tags='alert alert-success alert-dismissible fade show'
        )
        return redirect('core:mylibraries')

@login_required
def addLibrary(request):
    # user = models.User.objects.get(email = request.user.email)
    if request.method == "POST":
        form = forms.LibraryForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.owner = request.user

            new_form.save()
            messages.success(
                            request,
                            'Library Added Successfully',
                            extra_tags='alert alert-success alert-dismissible fade show'
                            )
            return redirect('core:mylibraries')

    form = forms.LibraryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/addlibrary.html', context)

@login_required
def deleteLibrary(request, id):
    library = get_object_or_404(models.library, id = id )
    if library.owner == request.user:
        library.delete()
        messages.success(
            request,
            'Property Deleted Successfully',
            extra_tags='alert alert-success alert-dismissible fade show'
        )
    else:
        messages.error(
            request,
            'You can not delete the property',
            extra_tags='alert alert-danger alert-dismissible fade show'
        )
    return redirect('core:mylibraries')

@login_required
def hideLibrary(request, id):
    library = get_object_or_404(models.library, id=id)
    if library.owner == request.user:
        library.visible = False
        library.save()
    return redirect('core:mylibraries')

@login_required
def showLibrary(request, id):
    library = get_object_or_404(models.library, id=id)
    if library.owner == request.user:
        library.visible = True
        library.save()
    return redirect('core:mylibraries')

@login_required
def BookmarkView(request):
    bookmarks = models.bookmark.objects.filter(user=request.user).first()
    context = {
        'bookmark': bookmarks,
    }
    return render(request, 'dashboard/bookmarks.html', context)

@login_required
def add_to_bookmark(request, id):
    library = get_object_or_404(models.library, id = id)
    bookmark_qs = models.bookmark.objects.filter(user = request.user)
    if bookmark_qs.exists():
        bookmark = bookmark_qs[0]
        if bookmark.libraries.filter(id = id).exists():
            messages.info(request, "Property Already Bookmarked")
        else:
            bookmark.libraries.add(library)
            messages.info(request, "Successfully Bookmarked")
    else:
        bookmark = models.bookmark.objects.create(user=request.user)
        bookmark.libraries.add(library)
        messages.info(request, "Successfully Bookmarked")
    return redirect("core:bookmarks")

@login_required
def remove_from_bookmark(request, id):
    library = get_object_or_404(models.library, id = id)
    bookmark_qs = models.bookmark.objects.filter(user = request.user)
    if bookmark_qs.exists():
        bookmark = bookmark_qs[0]
        if bookmark.libraries.filter(id = id).exists():
            bookmark.libraries.remove(library)
            messages.info(request, "Property removed from your Bookmarks")
    else:
        messages.info(request, "Property does not exist in your Bookmarks")
    return redirect("core:bookmarks")

@login_required
def ComparisonView(request):
    libraries = models.comaprison.objects.all()[:3]
    context = {
        'libraries': libraries,
    }
    return render(request, 'comparelibraries.html', context)

@login_required
def add_to_compare(request, id):
    library = get_object_or_404(models.library, id = id)
    compare_qs = models.bookmark.objects.filter(user = request.user)
    if compare_qs.exists():
        compare = compare_qs[0]
        if compare.libraries.filter(id = id).exists():
            messages.info(request, "Library Already Bookmarked")
        else:
            compare.libraries.add(library)
            messages.info(request, "Successfully Added to Compare")
    else:
        compare = models.bookmark.objects.create(user=request.user)
        compare.libraries.add(library)
        messages.info(request, "Successfully Added to Compare")
    return redirect("core:compare")

@login_required
def remove_from_compare(request, id):
    library = get_object_or_404(models.library, id = id)
    bookmark_qs = models.bookmark.objects.filter(user = request.user)
    if bookmark_qs.exists():
        bookmark = bookmark_qs[0]
        if bookmark.libraries.filter(id = id).exists():
            bookmark.libraries.remove(library)
            messages.info(request, "Property removed from your Bookmarks")
    else:
        messages.info(request, "Property does not exist in your Bookmarks")
    return redirect("core:bookmarks")

def TandCView(request):
    context = {}
    return render(request, 't&c.html', context)

def PrivacyPolicyView(request):
    context = {}
    return render(request, 'privacypolicy.html', context)



'''
#API
class AmmenitiesView(viewsets.ModelViewSet):
    queryset = models.ammenities.objects.all()
    serializer_class = serializers.AmmenitiesSerializer

class PaymentMethodsView(viewsets.ModelViewSet):
    queryset = models.payment_methods.objects.all()
    serializer_class = serializers.PaymentMethodsSerializer


class LibraryView(viewsets.ModelViewSet):
    queryset = models.library.objects.all()
    serializer_class = serializers.LibrarySerializer

class library_detail(viewsets.ModelViewSet):
    queryset = models.library.objects.all()
    serializer_class = serializers.LibrarySerializer
'''