from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField(max_length=200)
    department = models.CharField(max_length=50)
    created_by =  models.ForeignKey('auth.User',related_name='student',on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name 
