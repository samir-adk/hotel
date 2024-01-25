from django.urls import path
from resturant.views import room_filter,about_us,single_blog,blog_page,dashboard,book_now,contact,book_front
app_name='resturant'
urlpatterns=[
path('',dashboard,name='dashboard'),
path('book_now',book_now,name='book_now'),
path('contact',contact,name='contact'),
path('book_front/<int:id>',book_front,name='book_front'),
path('blog_page',blog_page,name='blog_page'),
path('single_blog/<int:id>',single_blog,name='single_blog'),
path('about_us',about_us,name='about_us'),
path('room_filter/<int:id>',room_filter,name='room_filter'),


]