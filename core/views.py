from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard(request: HttpRequest):
    context = {}
    return render(request, "dashboard/index.html")
