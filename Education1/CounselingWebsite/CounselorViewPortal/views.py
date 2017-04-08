

from django.template import loader

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    # all_students = Student.objects.all()
    #
    # template=loader.get_template('student/index.html')
    # context={
    #     'all_students':all_students
    # }
    return render(request,'CounselorViewPortal/index.html')
    # return HttpResponse(template.render(context,request))

def detail(request, studentId):
    return HttpResponse("<h2>Details for Student ID : " + str(studentId) + "</h2>")

class StudentLogin(CreateView):
    model=Student
    fields=['studentID','studentLName','studentMName','studentFName','studentEmailAddress','studentAge','studentDOB','street','city','zip','trackRepID','program']
