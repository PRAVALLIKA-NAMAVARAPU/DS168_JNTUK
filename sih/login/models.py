from django.db import models

# Create your models here.
class student(models.Model):
    gender=[('Male','Male'),('Female','Female')]
    classType=[('B.Tech','B.Tech'),('M.Tech','M.Tech')]
    studentRollno=models.CharField(max_length=100)
    studentName=models.CharField(max_length=100)
    studentGender=models.CharField(max_length=20,choices=gender)
    studentEmail=models.EmailField(max_length=100)
    date_birth=models.DateField(auto_now=True,null=True)
    studentClass=models.CharField(max_length=20,choices=classType)
    password=models.CharField(max_length=32)
    Due=models.IntegerField(null=False)
    def __str__(self):
        return self.studentName+" "+self.studentRollno
