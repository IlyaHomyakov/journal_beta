from django.shortcuts import render, HttpResponse
from datetime import datetime
import requests


def main_page(request):
    today_day = datetime.today().date().day
    today_month = datetime.today().date().month
    today_week_type = requests.get('http://127.0.0.1:8000/api/weektype/').json()  # IP сервера !
    if today_week_type['currentWeekType'] == 1:
        today_week_type = ', нечетная неделя'
    elif today_week_type['currentWeekType'] == 2:
        today_week_type = ', четная неделя'
    else:
        today_week_type = ''
    context = {
        'today_day': today_day,
        'today_month': today_month,
        'today_week_type': today_week_type
    }
    return render(request, 'main/index.html', context)
