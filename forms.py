from django import forms
from .models import NewUser

class FormNewUser(forms.ModelForm):
        class Meta:
            model= NewUser
            fields= ["firstname", "lastname", "email", "Username"]
