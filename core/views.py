from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity

from .models import Examinee, Test, Answer, Question
from itertools import chain


# Create your views here.
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


@login_required
def user_detail(request: HttpRequest, user_id: int):
    user: Examinee = get_object_or_404(Examinee, id=user_id)
    tests = Test.objects.all()
    context = {"examinee": user, "tests": tests}
    return render(request, "dashboard/user_info.html", context)


@login_required
def user_answers(request: HttpRequest, user_id: int, test_id: int):
    user: Examinee = get_object_or_404(Examinee, id=user_id)
    test = Test.objects.get(id=test_id)
    answers = Answer.objects.filter(examinee=user, question__test=test)
    answers_id = [answer.question.id for answer in answers]
    all_questions = list(
        chain(answers, Question.objects.filter(test=test).exclude(id__in=answers_id))
    )
    query = request.GET.get("query")
    if query:
        answers = answers.annotate(
            similarity=TrigramSimilarity("question__question", query)
        ).filter(similarity__gt=0.1)
    context = {"examinee": user, "test": test, "answers": all_questions}
    return render(request, "dashboard/test_info.html", context)


@login_required
def add_user(request: HttpRequest):
    return render(request, "dashboard/add_user.html")