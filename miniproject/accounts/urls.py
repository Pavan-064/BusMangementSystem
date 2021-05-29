from django.urls import path
from . import views

urlpatterns = [
   path('studentregistration',views.studentregistration,name = 'studentregistration'),
   path('studentlogin',views.studentlogin,name = 'studentlogin'),
   
   
]