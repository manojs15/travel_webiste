from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='log'),  # Login page URL
    path('register/',views.signup, name='signup'),  # Register page URL
    # Redirect GET requests # Add more URLs for other pages as needed
]
