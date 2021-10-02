from Store.models.products import Product
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db import models
from django.forms import fields
from .models.userprofile import UserProfile

class FarmerRegistrationForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']

class User_Form(UserChangeForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]
######------Extra Information-------------->>>>>>>

class InfoUserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('address', 'national_id_no', 'phone', 'image', 'national_id')




class CustomerRegForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =  "__all__"
    
#Question??
    # def is_Exist_email(self):
    #     email = self.Cleaned_data.get("email")
    #     user_count = User.objects.filter(email=email).count()
    #     if user_count > 0:
    #         raise forms.ValidationError('Sorry! this email already exits ')
    #     return email

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_stuff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    # last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'last_login', 'is_superuser', 'is_stuff', 'is_active','date_joined')
