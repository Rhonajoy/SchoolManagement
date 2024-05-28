from rest_framework import serializers
from .models import Class,ClassStream,Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','class_stream']
      

class ClassStreamSerializer(serializers.ModelSerializer):
    students=StudentSerializer(many=True,read_only=True)
    class Meta:
        model=ClassStream
        fields=['id', 'name', 'class_id', 'students']
        
class ClassSerializer(serializers.ModelSerializer):
    streams = ClassStreamSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ['id', 'name', 'streams']        
      
                