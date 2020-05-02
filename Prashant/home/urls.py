
from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name ='home-page'),
	path('login/', views.login, name = 'login-page'),
	path('logout/', views.logout, name = 'logout'),
	path('register/', views.register, name = 'signup-page'),
	path('profile/', views.profile, name = 'profile-page'),
	path('myContribution/', views.myContribution, name = 'myContribution'),
	path('edit/', views.edit, name = 'edit'),
]