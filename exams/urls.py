from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'exams'

urlpatterns = [
    #path('api/', include(router.urls)),

    #path('previous-years', views.HomeView, name='previous_year'),
    path('current-affairs', views.CurrentAffairsView, name='currentaffairs'),
    path('current-affairs/<int:id>', views.CurrentAffairView, name='currentaffair'),
    path('previous-years', views.PreviousYearQAView, name='previousyear'),
    path('download/<path>', views.download, name='download'),

]