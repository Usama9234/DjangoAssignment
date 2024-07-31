from django import forms
from django.forms import ModelForm
from .models import User,Message

class UserRegisterationForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'

class MessagingForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['senderName', 'ageBracket', 'message']