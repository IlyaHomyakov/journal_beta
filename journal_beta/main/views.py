from django.shortcuts import render, HttpResponse
from datetime import datetime
import requests


def main_page(request):
    today_date = datetime.today().date()

    context = {
        'today_date': today_date,
    }
    return render(request, 'main/index.html', context)
