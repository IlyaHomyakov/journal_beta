from django.shortcuts import render, HttpResponse
from datetime import datetime
import requests
from .models import *


def main_page(request):
    today_date = datetime.today().date()
    print()
    context = {
        'today_date': today_date,
        'title': MainPage.objects.values('title')[0]['title'],
        'help_text': MainPage.objects.values('help_text')[0]['help_text']
    }
    return render(request, 'main/index.html', context)
