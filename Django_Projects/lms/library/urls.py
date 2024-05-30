from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('books/<int:book_id>', views.book_details, name='book_details'),
    path('students/<int:student_id>', views.student_details, name='student_details'),
    path('all_students', views.all_student, name='all_student')
]