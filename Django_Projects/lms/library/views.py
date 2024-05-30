from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.
def homepage(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request, 'homepage.html', context)

def book_details(request, book_id):
    book = get_object_or_404(Book, pk = book_id)
    return render(request, 'book_details.html', {'book':book})

def student_details(request, student_id):
    student = get_object_or_404(Students, pk = student_id)
    borrows = Borrow.objects.filter(student = student)
    return render(request, 'student_details.html', {'student':student, 'borrows':borrows})

def all_student(request):
    students = Students.objects.all()
    return render(request, 'all_student.html', {'students':students})