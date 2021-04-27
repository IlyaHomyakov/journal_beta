import datetime
import json

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import SemesterOptions, Group, GroupLesson
from django.shortcuts import get_object_or_404


def get_group_schedule(request, got_group_number):
    get_object_or_404(Group, group_number=got_group_number)
    return_group_table_data = {
        "studentGroup": {
            "groupNumber": None,
            "facultyName": None,
            "course": None,
        },

        "tables": {
            "weekDay": {
                "Понедельник": {
                    "lessonList": [

                    ]
                },
                "Вторник": {
                    "lessonList": [

                    ]
                },
                "Среда": {
                    "lessonList": [

                    ]
                },
                "Четверг": {
                    "lessonList": [

                    ]
                },
                "Пятница": {
                    "lessonList": [

                    ]
                },
            }
        }
    }

    faculty_name = Group.objects.filter(group_number=got_group_number).values('faculty_choice').get()['faculty_choice']
    course = Group.objects.filter(group_number=got_group_number).values('course_choice').get()['course_choice']

    group_id = Group.objects.get(group_number=got_group_number).id

    group_table = GroupLesson.objects.filter(group_id_connector=group_id).values()

    return_group_table_data['studentGroup']['groupNumber'] = got_group_number
    return_group_table_data['studentGroup']['facultyName'] = faculty_name
    return_group_table_data['studentGroup']['course'] = course
    for i in range(len(group_table)):
        # print(return_group_table_data['tables']['weekDay']['Понедельник'])
        # if group_table[i]['week_day_choice'] in return_group_table_data['tables']['weekDay']:
        # print(inner_lesson_list['subject'])
        inner_lesson_list = {
            "subject": group_table[i]['subject'],
            "subjectType": group_table[i]['lesson_type_choice'],
            "weekType": group_table[i]['week_type_choice'],
            "specialDays": group_table[i]['special_days'],
            "auditory": group_table[i]['auditory'],
            "startLessonTime": group_table[i]['start_lesson_time'],
            "endLessonTime": group_table[i]['end_lesson_time'],
            "employee": {
                "fullName": group_table[i]['employee_full_name'],
                # "fio": None
            },
            "note": group_table[i]['note']
        }
        return_group_table_data['tables']['weekDay'][group_table[i]['week_day_choice']]['lessonList']\
            .append(inner_lesson_list)

    return JsonResponse(return_group_table_data)
    # return HttpResponse(group_table[0]['week_day_choice'])


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
