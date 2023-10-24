from django.urls import path
from . import views
from .views import add_marks, login_view, logout_view

urlpatterns = [
    #path('', views.home, name='home'),
    path('add_marks/', views.add_marks, name='add_marks'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
   
]
