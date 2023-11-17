from django.contrib.auth.forms import UserCreationForm
from django import forms
#from forms import ModelForm
from .models import *
from django.contrib.auth.models import User



class ListForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
       
        
        
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
       # fields = ['username','password1','password2']
        #widgets = {
            #"username": forms.TextInput(attrs={"class":"form-control"}),
            #"email": forms.EmailInput(attrs={"class":"form-control"}),
            #"password1": forms.PasswordInput(attrs={"class":"form-control"}),
            #3"password2": forms.PasswordInput(attrs={"class":"form-control"}),
            
        #}
       
        
        
    def save(self,commit = True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    
    
class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = '__all__'
        exclude = ["user"]
        
        
