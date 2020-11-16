from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {'class': 'form-control', 'data-validation-required-message': "Please enter your first name."})
        self.fields["last_name"].widget.attrs.update(
            {'class': 'form-control', 'data-validation-required-message': "Please enter your last name."})
        self.fields["email"].widget.attrs.update(
            {'class': 'form-control', 'data-validation-required-message': "Please enter your email."})
        self.fields["password1"].widget.attrs.update(
            {'class': 'form-control', 'data-validation-required-message': "Please enter your password."})
        self.fields["password2"].widget.attrs.update(
            {'class': 'form-control', 'data-validation-required-message': "Please confirm your password."})

    def save(self, commit=True):
        user = super().save(False)
        user.username = user.email.lower()
        user.email = user.email.lower()
        user = super().save()
        return user

    def clean(self):
        cd = self.cleaned_data

        email = cd.get("email").lower()
        print(cd)
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return cd
