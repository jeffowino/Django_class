from django import forms
from .models import Student, Attendance, Marks, Notice

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
