from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity
from django.forms import formset_factory


from .models import Examinee, Test, Answer, Question
from .forms import AddUserForm, SignInUserForm
from itertools import chain


# Create your views here.
# Dashboard : Home
@login_required
def dashboard(request: HttpRequest):
    query = request.GET.get("query")
    if query:
        examinees = Examinee.objects.annotate(
            similarity=TrigramSimilarity("name", query)
        ).filter(similarity__gt=0.1)
    else:
        examinees = Examinee.objects.all().order_by("-date")

    context = {"examinees": examinees}
    return render(request, "dashboard/index.html", context)


# Dashboard : User's information
@login_required
def user_detail(request: HttpRequest, user_id: int):
    user: Examinee = get_object_or_404(Examinee, id=user_id)
    tests = Test.objects.all()
    context = {"examinee": user, "tests": tests}
    return render(request, "dashboard/user_info.html", context)


# Dashboard : User's answers to a test
@login_required
def user_answers(request: HttpRequest, user_id: int, test_id: int):
    user: Examinee = get_object_or_404(Examinee, id=user_id) # Get user
    test = Test.objects.get(id=test_id) # Get test
    answers = Answer.objects.filter(examinee=user, question__test=test) # Get all of user for a test
    answers_id = [answer.question.id for answer in answers] # Get all of the answer's ids
    all_questions = list( # Get all of the questions for a test
        chain(answers, Question.objects.filter(test=test).exclude(id__in=answers_id))
    )
    context = {"examinee": user, "test": test, "answers": all_questions}
    return render(request, "dashboard/test_info.html", context)


@login_required
def add_user(request: HttpRequest):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            examinee = Examinee.objects.create(name=form.cleaned_data.get('name'))
            return redirect("core:dashboard")
    else:
        form = AddUserForm()
    context = {"form": form}
    return render(request, "dashboard/add_user.html", context)


# Home
def index(request: HttpRequest):
    if request.method == "POST":
        form = SignInUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            pass
    else:
        form = SignInUserForm()
    context = {"form": form}
    return render(request, "core/index.html", context)


# Do test
def do_test(request: HttpRequest, username:str, pk:int):
    test: Test = get_object_or_404(Test, id=pk)
    if request.method == "POST":
        breakpoint()

    context = {"test": test}
    return render(request, "core/test.html", context)
