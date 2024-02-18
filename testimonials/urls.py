from django.urls import path
from . import views

app_name = 'test' 

urlpatterns = [
    path('testimonials/', views.testimonials, name='testi')
]
