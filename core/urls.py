from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'core'

'''
router = DefaultRouter()
router.register('ammenities', views.AmmenitiesView,  basename='ammenities')
router.register('payment_methods', views.PaymentMethodsView,  basename='payment_methods')
router.register('library', views.LibraryView, basename='library')
'''
urlpatterns = [
    #path('api/', include(router.urls)),
    path('', views.HomeView, name='home'),
    path('contact', views.ContactView, name='contact'),
    path('libraries', views.LibrariesView, name='libraries'),
    path('library/<int:id>', views.LibraryView, name='library'),


    path('user-profile', views.UserProfileView, name='userprofile'),
    path('my-libraries', views.myLibraries, name='mylibraries'),
    path('hide-library/<int:id>', views.hideLibrary, name='hidelibrary'),
    path('show-library/<int:id>', views.showLibrary, name='showlibrary'),

    path('my-bookmarks', views.BookmarkView, name='bookmarks'),
    path('add-to-bookmarks/<int:id>', views.add_to_bookmark, name='addtobookmarks'),
    path('remove-from-bookmarks/<int:id>', views.remove_from_bookmark, name='removefrombookmarks'),

    path('addlibrary', views.addLibrary, name='addlibrary'),
    path('editlibrary/<int:id>', views.editLibrary, name='editlibrary'),
    path('deletelibrary/<int:id>', views.deleteLibrary, name='deletelibrary'),

]
