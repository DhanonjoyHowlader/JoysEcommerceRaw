from django import forms
from .models import Profile

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ('Full_name','Mobile_number','Profile_Picture','Email_address','Date_of_Birth','Gender','Billing_address')