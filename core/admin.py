from django.contrib import admin

from .models import Answer, Test, Examinee, Question, Choice


admin.site.index_title = "Site admin"
admin.site.site_title = "Administration"
admin.site.site_header = "Administration"


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0



# Register your models here
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "date"]
    list_display_links = ["title" ,"date"]
    list_filter = ["date"]

    ordering = ["date"]

    date_hierarchy = "date"

    search_fields = ["title"]

    inlines = (ChoiceInline, QuestionInline)


@admin.register(Examinee)
class ExamineeInline(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = list_display
    inlines = (AnswerInline,)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "test", Question.__str__]
    list_display_links = list_display


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "examinee", "question", "choice"]
    list_display_links = ["examinee", "question"]
    list_filter = ["choice__text", "examinee"]

    search_fields = ["examinee"]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "score","test"]
    list_editable = ["text", "score"]
    list_display_links = ["test"]
    list_filter = ["test"]

    search_fields = ["test"]
