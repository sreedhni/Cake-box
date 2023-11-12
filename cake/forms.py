from django import forms
from django.contrib.auth.forms import UserCreationForm
from cake.models import User,CakeCategory,CakeOccation,CakeVarient,CakeOrder


class RegistrtionForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone","adress"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


class CakeCategoryForm(forms.ModelForm):
    class Meta:
        model=CakeCategory
        fields=["name"]


class CakeOccationForm(forms.ModelForm):
    class Meta:
        model=CakeOccation
        fields="__all__"

class CakeVarientForm(forms.ModelForm):
    class Meta:
        model=CakeVarient
        exclude=("occation",) #tuple is immutable so tuble is used,updation not allowed

