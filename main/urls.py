from . import views

from django.urls import path

urlpatterns = [
    path('home', views.home, name='home'),
    path('logout', views.logoutUser, name='logout'),
    path('base', views.base, name='base'),
    path('login', views.account, name='login'),
    path('staff', views.staff, name='staff'),
    path('about', views.about, name='about'),
    path('detail', views.detail, name='detail'),
    path('admission', views.admission, name='admission'),
    path('parent', views.parent, name='parent'),
    path('new_password', views.change_password, name='new_password'),

]