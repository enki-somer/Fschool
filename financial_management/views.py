from django.shortcuts import render, redirect
from .models import Student, Teacher, Payment, Salary
from .forms import StudentForm, TeacherForm, PaymentForm, SalaryForm

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers_list')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})
