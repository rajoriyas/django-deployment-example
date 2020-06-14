from django.urls import path
from first_app_with_password import views

app_name = 'first_app_with_password'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
]
