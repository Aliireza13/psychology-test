from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "تست"
        verbose_name_plural = "تست ها"


class Examinee(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "شرکت کننده"
        verbose_name_plural = "شرکت کنندگان"



class Question(models.Model):
    test = models.ForeignKey(
        to=Test, on_delete=models.CASCADE, related_name="questions"
    )
    question = models.TextField()

    def __str__(self) -> str:
        return (" ".join(self.question.split()[:5])) + " ..."

    class Meta:
        verbose_name = "سوال"
        verbose_name_plural = "سوال ها"


class Choice(models.Model):
    test = models.ForeignKey(
        to=Test, on_delete=models.CASCADE, related_name="choices"
    )

    text = models.CharField(max_length=255)
    score = models.PositiveIntegerField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "گزینه"
        verbose_name_plural = "گزینه ها"


class Answer(models.Model):
    examinee = models.ForeignKey(
        to=Examinee, on_delete=models.CASCADE, related_name="answers", verbose_name="شرکت کننده"
    )

    question = models.ForeignKey(
        to=Question, on_delete=models.CASCADE, related_name="answers", verbose_name="سوال"
    )

    choice = models.ForeignKey(
        to=Choice, on_delete=models.CASCADE, related_name="answers", verbose_name="گزینه"
    )

    def __str__(self) -> str:
        return self.choice.text

    class Meta:
        verbose_name = "جواب"
        verbose_name_plural = "جواب ها"
