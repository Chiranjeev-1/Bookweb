from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class Usercreateform(UserCreationForm):
    class Meta:
        model = User
        



        fields = ['username','password1','password2',]
        widgets = {
            'username':forms.TextInput(attrs={'class':'inputfield'}),
            'password1':forms.PasswordInput(attrs={'class':'inputfield'}),
            'password2':forms.PasswordInput(attrs={'class':'inputfield'})
        }


class statusuploadform(ModelForm):
    class Meta:
        
        model = Statusupload
        
        fields = ["status",'score',"startdate","completedate","note"]
        

class Bioform(ModelForm):
    class Meta:
        model = Bio
        fields= ["username","profileimage","Banner","selfdescription"]


class Postform(ModelForm):
    class Meta:
        model = OriginalPOST
        fields = ['post','posttype']



class Forumdataform(ModelForm):
    class Meta:
        model = Forumdata
        fields = ['post','posttitle']
        widgets = {
            'posttitle':forms.TextInput(attrs={'placeholder':'POST TITLE'}),
            'post':forms.TextInput(attrs={'placeholder':'POST Description'})
        }


class subscriptionform(ModelForm):
    class Meta:
        model = OriginalPOST
        fields = ["authorname","post","posttype","Bookcover","Synopsis","Booktitle","UpforReview"]
        widgets = {
            'Synopsis':forms.TextInput(attrs={'placeholder':'Synopsis'}),
            
        }