from django.shortcuts import render, HttpResponse
from datetime import datetime


def main_page(request):
    today_day = datetime.today().date().day
    today_month = datetime.today().date().month
    context = {
        'today_day': today_day,
        'today_month': today_month,
    }
    return render(request, 'main/index.html', context)


