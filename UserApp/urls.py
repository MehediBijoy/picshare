from django.urls import path
from . import views


urlpatterns = [
    path('userRegistration/', views.UserRegistration, name='user_register'),
    path('loginView/', views.loginView.as_view(), name='login'),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('<str:username>/', views.profileView, name='profile'),
]
