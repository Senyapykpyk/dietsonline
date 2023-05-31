from django import forms
from django.contrib.auth.models import User
from .models import SiteUser
from .models import ProfileConsultant
from .models import ProfileUser
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = SiteUser
        fields = ['username', 'email', 'password1', 'password2', 'is_consultant']

class ConsultantProfileForm(forms.ModelForm):
    firstname = forms.CharField(label="Имя")
    lastname = forms.CharField(label="Фамилия")
    surname = forms.CharField(label="Отчество")

    class Meta:
        model = ProfileConsultant
        fields = ['firstname','lastname','surname','education','experience','description', 'image']

class UserProfileForm(forms.ModelForm):
    firstname = forms.CharField(label="Имя")
    lastname = forms.CharField(label="Фамилия")
    surname = forms.CharField(label="Отчество")
    # iterable
    
   
    class Meta:
        model = ProfileUser
        fields = ['firstname','lastname','surname','sex', 'bday','height','weight', 'image']
