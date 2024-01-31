from django.contrib import admin

from .models import Answer, Test, Examinee, Question


admin.site.index_title = "Site admin"
admin.site.site_title = "Administration"
admin.site.site_header = "Administration"


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0


# Register your models here
@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ["title", "date"]
    list_display_links = ["title" ,"date"]
    list_filter = ["date"]

    ordering = ["date"]

    date_hierarchy = "date"

    search_fields = ["title", "author__first_name", "author__last_name"]


@admin.register(Examinee)
class ExamineeInline(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = list_display
    inlines = (AnswerInline,)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["test", Question.__str__]
    list_display_links = list_display


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["examinee", "question", "choice"]
    list_editable = ["choice"]
    list_display_links = ["examinee", "question"]
    list_filter = ["choice", "examinee"]

    search_fields = ["examinee"]
    raw_id_fields = ["question"]
