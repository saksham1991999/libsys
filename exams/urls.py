from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'exams'

urlpatterns = [
    #path('api/', include(router.urls)),

    #path('previous-years', views.HomeView, name='previous_year'),
    path('test', views.testView, name='test'),
    path('current-affairs', views.CurrentAffairsView, name='currentaffairs'),
    path('previous-years', views.PreviousYearQAView, name='previousyear'),
    # path('download/<int:id>/<int:no>', views.download, name='download'),

]