from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Class,ClassStream,Student
from .serializers import ClassSerializer,ClassStreamSerializer,StudentSerializer

# Create your views here.
@api_view(['GET','POST'])
def create_view_class(request):
    if request.method=='GET':
         classes=Class.objects.all()
         serializer=ClassSerializer(classes,many=True)
         return Response(serializer.data)
    elif request.method=='POST':
        serializer=ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def create_view_streams(request):
    if request.method == 'GET':
        streams = ClassStream.objects.all()
        serializer = ClassStreamSerializer(streams, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClassStreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_a_stream(request, pk):
    try:
        stream = ClassStream.objects.get(pk=pk)
    except ClassStream.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClassStreamSerializer(stream)
        return Response(serializer.data)
 

@api_view(['GET', 'POST'])
def create_view_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_a_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def view_students_by_stream(request, stream_id):
    try:
        stream = ClassStream.objects.get(pk=stream_id)
        print(stream)
    except ClassStream.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    students = Student.objects.filter(class_stream=stream)
    print(students)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
    
     
                  
          
          