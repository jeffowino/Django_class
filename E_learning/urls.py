from django.urls import path
from . import views
from .views import add_marks,home, login_view, logout_view, dashboard, enroll_subject, upload_assignment, create_notice

urlpatterns = [
    # Existing paths
    path('', views.home, name='home'),
    path('add_marks/', add_marks, name='add_marks'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # New paths
    path('dashboard/', dashboard, name='dashboard'),
    path('enroll_subject/<int:subject_id>/', enroll_subject, name='enroll_subject'),
    path('upload_assignment/', upload_assignment, name='upload_assignment'),
    path('create_notice/', create_notice, name='create_notice'),
]
