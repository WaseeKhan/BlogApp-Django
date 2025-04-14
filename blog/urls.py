from django.urls import path
from .views import *

app_name ='blog'

urlpatterns = [
    path("", home, name='home'),
    path("post/<int:year>/<int:month>/<int:day>/<slug:slug>/", post_detail, name='post_detail'),
] 
