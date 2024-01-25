from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity

from .models import Examinee, Test


# Create your views here.
@login_required
def dashboard(request: HttpRequest):
    query = request.GET.get("query")
    if query:
        examinees = Examinee.objects.annotate(
            similarity=TrigramSimilarity("name", query)
        ).filter(similarity__gt=0.05)
    else:
        examinees = Examinee.objects.all().order_by("-date")

    context = {"examinees": examinees}
    return render(request, "dashboard/index.html", context)


@login_required
def user_detail(request: HttpRequest, pk: int):
    user: Examinee = get_object_or_404(Examinee, id=pk)
    tests = Test.objects.all()
    context = {"examinee": user, "tests": tests}
    return render(request, "dashboard/user_info.html", context)
