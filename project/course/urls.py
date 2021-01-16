from django.urls import path
from course.views import allcourse,addcourse

urlpatterns = [
    path('', allcourse, name='courseindex'),
  
    path('add/', addcourse, name='courseadd'),

]