from django import forms
from .models import Student, Attendance, Marks, Notice, Teacher, Subject, Enrollment, Assignment, AttendanceHistory  # Updated import

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

class TeacherForm(forms.ModelForm):  # New form for Teacher
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectForm(forms.ModelForm):  # New form for Subject
    class Meta:
        model = Subject
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):  # New form for Enrollment
    class Meta:
        model = Enrollment
        fields = '__all__'

class AssignmentForm(forms.ModelForm):  # New form for Assignment
    class Meta:
        model = Assignment
        fields = '__all__'

class AttendanceHistoryForm(forms.ModelForm):  # New form for AttendanceHistory
    class Meta:
        model = AttendanceHistory
        fields = '__all__'
