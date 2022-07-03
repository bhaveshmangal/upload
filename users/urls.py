from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/<str:pk>/', views.profile, name="profile"),
    path('account/', views.userAccount, name="account"),
    path('profiles/', views.profiles, name="profiles"),
    path('edit-account/', views.editAccount, name="edit-account"),
]