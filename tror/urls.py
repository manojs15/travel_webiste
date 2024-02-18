from django.urls import path
from . import views

app_name = 'tror'

urlpatterns = [
    path('order/', views.ord_form, name='order'),
    path('success/', views.success_view, name='success'),
    path('done/', views.done_view, name='done'),
    path('ord_details/<int:order_id>/', views.order_details, name='order_details')
]
