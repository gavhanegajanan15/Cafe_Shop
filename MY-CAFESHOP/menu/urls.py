from django.urls import path
from . import views   # make sure this line exists

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_list, name='menu'),
    path('special/', views.special, name='special'),
    path('gallery/', views.gallery, name='gallery'),
    path('book_table/', views.book_table, name='book_table'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
