from django import forms
from . models import User
# from django.forms import ModelForm


class NameForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=32)

class UserForm(forms.ModelForm):

    
    # say what is our models refrences??
    class Meta:
        model = User
        fields = "__all__"
        # fields = ["email", "password"]
        exclude = ["permission", "description"]

    