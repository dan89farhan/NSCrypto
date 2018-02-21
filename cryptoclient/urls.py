from django.urls import path
from . import views

app_name = 'cryptoclient'
urlpatterns = [
    path('', views.index, name = "index"),
    path('register/', views.register, name='register'),
    path('yourname/', views.get_name, name= 'yourname'),
    path('<int:pk>/thanks/', views.ThanksView.as_view(), name= 'thanks'),
    path('contactform/', views.contactform, name='contactform'),
    path('encrypt/', views.encrypt, name="encrypt"),
    path('decrypt/', views.decrypt, name= 'decrypt'),
    path('<int:pk>/', views.EncryptedView.as_view(), name = 'test'),
]