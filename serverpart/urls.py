from django.urls import path
from . import views
urlpatterns = [
	path('', views.home_page, name='home'),
	path('test/', views.test_page),
	path('testforming/', views.test_creation_page, name='testforming'),

	
	path('signup/', views.signupuser, name='signup'),
	path('logout/', views.logoutuser, name='logout'),
	path('login/', views.loginuser, name='login'),
]
