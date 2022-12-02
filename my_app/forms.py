from django import forms
from .models import Debate , User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class DebateForm(forms.ModelForm):
    class Meta:
        model = Debate
        fields = ['id' ,'title', 'description', 'status']