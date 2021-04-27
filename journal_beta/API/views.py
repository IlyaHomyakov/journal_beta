import datetime
import json

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import SemesterOptions, Group, GroupLesson
from django.shortcuts import get_object_or_404
from . import return_group_json_template


def get_group_schedule(request, got_group_number):
    get_object_or_404(Group, group_number=got_group_number)
    return_group_table_data = return_group_json_template.return_data
    faculty_name = Group.objects.filter(group_number=got_group_number).values('faculty_choice').get()['faculty_choice']
    course = Group.objects.filter(group_number=got_group_number).values('course_choice').get()['course_choice']

    group_id = Group.objects.get(group_number=got_group_number).id

    group_table = GroupLesson.objects.filter(group_id_connector=group_id).values()

    return_group_table_data['studentGroup']['groupNumber'] = int(got_group_number)
    return_group_table_data['studentGroup']['facultyName'] = faculty_name
    return_group_table_data['studentGroup']['course'] = int(course)
    for x in range(len(group_table)):
    #     if 'Понедельник' in group_table[x].values() and 'Понедельник' not in return_group_table_data['tables']['weekDay']:
        print(x)

    # return JsonResponse(return_group_table_data)
    return HttpResponse(group_table.values())


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
            return_data['currentWeekType'] = tmp + 1
            i += 1
    else:
        tmp = int(start_week_type)
        while i <= current_week:
            tmp = 1 - tmp
            return_data['currentWeekType'] = tmp - 1
            i += 1

    return JsonResponse(return_data)


def api_main_page(request):
    return HttpResponse('Вы попали на главную страницу API BSMU JOURNAL\n'
                        'Сама по себе она бесполезна.\n'
                        'Вот некоторые команды API:\n'
                        '/weektype возвращает тип текущей недели\n'
                        '/get_group_table/<номер группы> возвращает расписание группы\n'
                        'Формат json')
