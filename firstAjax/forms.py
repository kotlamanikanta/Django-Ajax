from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "course"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "nameid",
                    "onchange": "onFunction()",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "emailid",
                    "onchange": "onFunction()",
                }
            ),
            "course": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "courseid",
                    "onchange": "onFunction()",
                }
            ),
        }
