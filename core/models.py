from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Test(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="tests")
    title = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Examinee(models.Model):
    name = models.CharField(max_length=255)


class Question(models.Model):
    test = models.ForeignKey(
        to=Test, on_delete=models.CASCADE, related_name="questions"
    )
    question = models.TextField()

    def __str__(self) -> str:
        return self.question.split()[:5]


class Answer(models.Model):
    class Choices(models.TextChoices):
        A = "A", "A"
        B = "B", "B"
        C = "C", "C"
        D = "D", "D"

    question = models.ForeignKey(
        to=Question, on_delete=models.CASCADE, related_name="answers"
    )
    examinee = models.ForeignKey(
        to=Examinee, on_delete=models.CASCADE, related_name="answers"
    )
    choice = models.CharField(choices=Choices.choices, max_length=255)
