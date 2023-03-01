
from django.urls import path
from django.urls import include, path
from . import views
urlpatterns = [
  path('login/',views.LoginPage,name='login'),
  path('',views.HomePage,name='home'),
  path('home/',views.HomePage,name='home'),
  path('logout/',views.LogoutPage,name='logout'),
  path('contact/', views.contact_view, name='contact'),
  path('signup/', views.SignupPage, name='signup'),
]
