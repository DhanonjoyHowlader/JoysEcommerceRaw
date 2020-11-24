from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    Full_name = models.CharField(max_length=50)
    Mobile_number = models.CharField(max_length=30)
    Profile_Picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    Email_address = models.CharField(max_length=100,blank=True, null=True)
    Date_of_Birth = models.DateField()
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHER = 3
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),(GENDER_OTHER, 'Other')]
    Gender = models.IntegerField(choices=GENDER_CHOICES)
    Billing_address = models.TextField(max_length=500)

    Username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.Username.username



