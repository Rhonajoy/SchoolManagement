from django.urls import path
from . import views 



urlpatterns = [
    path('classes', views.create_view_class, name='class_view_class'),
    path('streams', views.create_view_streams, name='create_view_streams'),
    path('streams/<int:pk>', views.get_a_stream, name='get_stream'),
    path('students',views.create_view_students, name='create_view_students'),
    path('students/<int:pk>', views.get_a_student, name='get_student'),
    path('streams/<int:stream_id>/students', views.view_students_by_stream, name='students_by_stream'),
    
]