from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update(
            {'class': 'form-control','data-validation-required-message':"Please enter your first name."})
        self.fields["last_name"].widget.attrs.update(
            {'class': 'form-control','data-validation-required-message':"Please enter your last name."})
        self.fields["email"].widget.attrs.update(
            {'class': 'form-control','data-validation-required-message':"Please enter your email."})
        self.fields["password1"].widget.attrs.update(
            {'class': 'form-control','data-validation-required-message':"Please enter your password."})
        self.fields["password2"].widget.attrs.update(
            {'class': 'form-control','data-validation-required-message':"Please confirm your password."})
