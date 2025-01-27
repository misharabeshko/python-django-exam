from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "password"]

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return make_password(password)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def authenticate(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if check_password(password, user.password):
            return user
        return None
