from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Postcode = models.CharField(max_length=10)
    DOB = models.DateField('date of birth (MM/DD/YYYY)')
    Username = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)

class Event(models.Model):
	Postcode = models.CharField(max_length=10)
	Game = models.CharField(max_length=100)
	Description = models.CharField(max_length=1000)
	Min_Age = models.IntegerField()
	Time_Date = models.DateTimeField('time and date of event')
	Verified = models.CharField(max_length=1)
	People_Limit = models.IntegerField()
	People_Attending = models.IntegerField()
	Owner_user_ID = models.IntegerField()

