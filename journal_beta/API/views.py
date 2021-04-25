import datetime

from django.http import HttpResponse
from .models import SemesterOptions
from time import strftime


def index(request):
    return HttpResponse("Первая страница")


def week_type(request):
    start_day = SemesterOptions.objects.get(semester_start__year=datetime.date.today().year)
    print(start_day)
    return HttpResponse(strftime("%V"))
    # return '1'
