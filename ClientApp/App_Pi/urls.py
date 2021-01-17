from django.urls import path
from App_Pi import views 

urlpatterns = [
    path('',views.index,name='index'),
]