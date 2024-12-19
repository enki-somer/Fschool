from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)
    grade = models.CharField(max_length=100)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    arabic_name = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.amount} on {self.date_paid}"

class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField()

    def __str__(self):
        return f"{self.teacher.name} - {self.amount} on {self.date_paid}"
