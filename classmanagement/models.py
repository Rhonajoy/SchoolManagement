from django.db import models

# Create your models here.
class Class(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class ClassStream(models.Model):
    name=models.CharField(max_length=10)
    class_id=models.ForeignKey(Class,related_name='streams',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    class_stream=models.ForeignKey(ClassStream,related_name='students',on_delete=models.CASCADE)   
    
    def __str__(self):
        return self.name 
        