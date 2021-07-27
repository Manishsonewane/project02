
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blogdetails',views.blogdetails,name='blogdetails'),
    path('blogstandard',views.blogstandard,name='blogstandard'),
    path('contact',views.contact, name='contact'),
    path('faq',views.faq,name='faq'),
    path('gallery',views.gallery, name='gallery'),
    path('index2',views.index2,name='index2'),
    path('manu',views.manu,name='manu'),
    path('restaurantdetails',views.restaurantdetails,name='restaurantdetails'),
    path('restaurant',views.restaurant,name='restaurant'),
    path('team',views.team,name='team')

    
]
