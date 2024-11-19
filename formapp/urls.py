from django.urls import path
from .views import my_form_view,success_url

urlpatterns = [
    path('myform/', my_form_view, name='myform'),
path('success_url/', success_url, name='success_url'),

# path('myform/', initialview, name='myform'),
]
