from django.urls import path
from . import views

app_name = "websiteUrls"

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('appointment/', views.appointment, name="appointment"),
    path('price/', views.price, name="price"),
    path('services/', views.services, name="services"),
    path('team/', views.team, name="team"),
    path('testimonial/', views.testimonial, name="testimonial"),


]
