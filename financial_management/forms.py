from django import forms
from .models import Student, Teacher, Payment, Salary

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'arabic_name', 'grade', 'tuition_fee', 'paid']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'arabic_name', 'salary']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount', 'date_paid']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['teacher', 'amount', 'date_paid']
