from django.shortcuts import render
from .models import Student

def student_views(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students/index.html', context)
