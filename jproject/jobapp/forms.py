from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    qualification = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    experience = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    skills = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    resume = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text=None,
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text=None,
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'phone_number', 
            'qualification', 'experience', 'skills', 'resume', 'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}),
        }

class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'username', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
        }      






class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    phone_number = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    skills = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    resume = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))