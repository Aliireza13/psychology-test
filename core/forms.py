from django.shortcuts import get_object_or_404
from django.http import Http404
from django import forms
from .models import Examinee


# Create your forms here.
class AddUserForm(forms.Form):
    name = forms.CharField(max_length=255, min_length=2, strip=True, required=True)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        try:
            exist = get_object_or_404(Examinee, name=name)
        except Http404:
            return name
        else:
            raise forms.ValidationError(
                f"کاربر '{name}'  وجود دارد لطفا اسم دیگری وارد کنید"
            )


class SignInUserForm(AddUserForm):
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        try:
            examinee = get_object_or_404(Examinee, name=name)
        except Http404:
            raise forms.ValidationError(f"کاربری با اسم \"{name}\" ثبت نشده است!")
        return name
