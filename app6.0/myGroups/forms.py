from django import forms
from django.forms import ModelForm

from .models import Groups, Students


class GroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = "__all__"
        labels = {
            "name": "Ingresa grupo y grado"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control col-sm-4"}),
        }


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        labels = {
            "name": "Nombre/s",
            "last_name": "Apellido Paterno",
            "second_last_name": "Apellido Materno",
            "group": "Grupo",
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control col-lg-4"}),
            "last_name": forms.TextInput(attrs={"class": "form-control col-lg-4"}),
            "second_last_name": forms.TextInput(attrs={"class": "form-control col-lg-4"}),
            "group": forms.Select(attrs={"class": "form-control col-lg-4"}),
        }