from django import forms

class loginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)

class emailForm(forms.Form):
	email_address = forms.EmailField(max_length=254)