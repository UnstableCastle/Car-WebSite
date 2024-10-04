from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('add/', views.add_car, name='add_car'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Add this line for logout
]
