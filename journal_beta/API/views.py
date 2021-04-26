import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import SemesterOptions


def index(request):
    return HttpResponse("Первая страница")


def week_type(request):
    semester_opts = SemesterOptions.objects.values().get()
    start_week_type = semester_opts['server_week_type_choice']
    semester_start_week = semester_opts['semester_start'].isocalendar()[1]
    current_week = datetime.date.today().isocalendar()[1]

    return_data = {
        'currentWeekType': None
    }
    i = semester_start_week
    if int(start_week_type) == 1:
        tmp = int(start_week_type)
        while i <= current_week:
            tmp = 1 - tmp
            print(tmp + 1, " ")
            return_data['currentWeekType'] = tmp + 1
            i += 1
    else:
        tmp = int(start_week_type)
        while i <= current_week:
            tmp = 1 - tmp
            print(tmp - 1, " ")
            return_data['currentWeekType'] = tmp - 1
            i += 1

    return JsonResponse(return_data)
