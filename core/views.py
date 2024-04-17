from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity
from django.forms import formset_factory


from .models import Examinee, Test, Answer, Question
from .forms import AddUserForm, SignInUserForm, FourChoiceAnsForm, FiveChoiceAnsForm
from . utils import is_test_done
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
            test = Test.objects.first()
            return redirect("core:check_user", username=name)
    else:
        form = SignInUserForm()
    context = {"form": form}
    return render(request, "core/index.html", context)


def check_user(request: HttpRequest, username: str):
    tests = Test.objects.all()
    examinee = get_object_or_404(Examinee, name=username)
    for test in tests:
        if not is_test_done(test, examinee):
            return do_test(request, examinee, test)
    return success(request, examinee)


def success(request: HttpRequest, examinee: Examinee):
    return render(request, "core/test_done.html", {"examinee": examinee})


def do_test(request: HttpRequest, examinee: Examinee, test: Test):
    context = {}
    context.update({"test": test})

    c_choice = test.choices.count() # Number of available choices for given test
    if c_choice == 4:
        form = FourChoiceAnsForm
    elif c_choice == 5:
        form = FiveChoiceAnsForm
    q_count = test.questions.count() # Number of available questions for given test
    FormSet = formset_factory(form, extra=q_count, min_num=q_count, max_num=q_count)

    if request.method == "POST":
        formset = FormSet(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            questions = test.questions.all()
            for i in range(q_count):
                score = data[i].get("answer")
                q = questions[i]
                choice = test.choices.get(score=score)
                answer = Answer.objects.create(
                    examinee=examinee,
                    question=q,
                    choice=choice
                )
            return redirect("core:check_user", username=examinee.name)
    else:
        formset = FormSet()

    context.update({"formset": formset})
    return render(request, "core/test.html", context)
