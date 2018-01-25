from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('register/', views.register, name='register'),
    path('yourname/', views.get_name, name= 'yourname'),
    path('thanks/', views.thankspage, name= 'thanks'),
    path('contactform/', views.contactform, name='contactform'),
    path('cryptons/', views.crypto, name="cryptons"),
    path('plaintext/', views.decrypt, name= 'plaintext')
]