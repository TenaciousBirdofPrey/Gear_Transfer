#http://stackoverflow.com/questions/11923317/creating-django-forms

from django import forms

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)