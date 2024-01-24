from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from . models import Examinee

# Create your views here.
@login_required
def dashboard(request: HttpRequest):
    examinees = Examinee.objects.all()
    context = {'examinees': examinees}
    return render(request, "dashboard/index.html", context)
