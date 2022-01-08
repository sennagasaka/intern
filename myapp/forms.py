from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import Talk

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["image"].required = False
        self.fields["email"].required = True

    class Meta:
        model=get_user_model()
        fields=('username','email', 'image','password1', 'password2')
        labels={
            'username':'名前',
            'image':'画像',
            'password1':'パスワード',
            'password2':'パスワード(確認用)',
        }
        

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
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

class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'