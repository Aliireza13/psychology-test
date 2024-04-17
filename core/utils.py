from .models import Test, Answer


def has_next_test(test_id):
    "Check if there is a newer test"
    next = Test.objects.filter(id__gt=test_id).first()
    if next: return next
    else: return False


def has_previous_test(test_id):
    "Check if there is an older test"
    next = Test.objects.filter(id__lt=test_id).first()
    if next: return next
    else: return False


def is_test_done(test, examinee):
    "Check if examinee has done given test"
    next = Answer.objects.filter(question__test=test, examinee=examinee)
    if next: return True
    else: return False

