from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Student(models.Model):
    studentID = models.CharField(max_length=10)
    studentLName = models.CharField(max_length=50)
    studentMName = models.CharField(max_length=50)
    studentFName = models.CharField(max_length=50)
    studentEmailAddress = models.CharField(max_length=50)
    studentAge = models.CharField(max_length=3)
    studentDOB = models.DateField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    trackRepID = models.CharField(max_length=50)
    program = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("student:index")
    def __str__(self):
        return self.studentID

class Counselor(models.Model):
    counselorID = models.CharField(max_length=10)
    counselorLName = models.CharField(max_length=50)
    counselorMName = models.CharField(max_length=50)
    counselorFName = models.CharField(max_length=50)
    def __str__(self):
        return self.counselorID
class Appointment(models.Model):
    appointmentID = models.CharField(max_length=10)
    studentID = models.CharField(max_length=10)
    counselorID = models.CharField(max_length=10)
    aStartTime = models.DateTimeField(max_length=10)
    aEndTime = models.DateTimeField(max_length=50)
    aDate = models.DateTimeField(max_length=50)
    requestId = models.CharField(max_length=10)
    requestType = models.CharField(max_length=50)
    timeOfSubmittingRequest = models.DateTimeField(max_length=50)
    requestDate = models.DateTimeField(max_length=50)
    requestStartTime = models.DateTimeField(max_length=50)
    requestEndTime = models.DateTimeField(max_length=50)
    def __str__(self):
        return self.appointmentID
class Profile(models.Model):
    profileID = models.CharField(max_length=10)
    studentID = models.CharField(max_length=10)
    Cat = models.CharField(max_length=50)
    Seq = models.CharField(max_length=100)
    Label = models.CharField(max_length=100)
    Value = models.CharField(max_length=100)
    def __str__(self):
        return self.profileID