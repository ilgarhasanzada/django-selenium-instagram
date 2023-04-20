from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    path('login/', views.SignInView.as_view(), name = 'login'),
    path('register/', views.SignUpView.as_view(), name = 'register'),
    path('logout/', views.logout_view, name = 'logout'),
    path('add_instagram/', views.AddInstagramView.as_view(), name = 'add_instagram'),
    path('update_instagram/', views.UpdateInstagramView.as_view(), name = 'update_instagram'),
]