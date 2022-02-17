from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import (
    SignupForm,
    LoginForm,
    ChangePasswordForm,
)
from .models import User,Talk

class SignupForm(SignupForm):
    img = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'img')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = field.label

class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = field.label



class TalkForm(forms.ModelForm):
    class Meta:
        model=Talk
        fields=('talk',)
        widgets= {"talk": forms.TextInput(attrs={"autocomplete": "off"})}


class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model=User
        fields=("username",)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = field.label
    
class EmailChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ImageChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PasswordChangeForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class FindForm(forms.Form):
    find=forms.CharField(label='Find',required=False)