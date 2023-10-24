from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import StudentForm, AttendanceForm, MarksForm, NoticeForm
from .models import Student, Attendance, Marks, Notice
from django.http import HttpResponse

def add_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marks added successfully.')
            return redirect('add_marks')
    else:
        form = MarksForm()
    return render(request, 'add_marks.html', {'form': form})

def login_view(request):
    return HttpResponse('Testing the login page')

def home(request):
    return HttpResponse('Testing the home page')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')
