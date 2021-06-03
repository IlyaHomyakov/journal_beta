import datetime
from django.http import JsonResponse, HttpResponse
from .models import Group, GroupLesson
from django.shortcuts import get_object_or_404


def get_group_schedule(request, got_group_number):
    return_group_table_data = {
        "studentGroup": {
            "groupNumber": None,
            "facultyName": None,
            "course": None,
        },
        "tables": {
            "weekDay": {
                "Понедельник": {
                    "lessonList": []
                },
                "Вторник": {
                    "lessonList": []
                },
                "Среда": {
                    "lessonList": []
                },
                "Четверг": {
                    "lessonList": []
                },
                "Пятница": {
                    "lessonList": []
                },
            },
            "semesterStartDate": None,
            "semesterEndDate": None,
            "isWeekTypeNeeded": None,
            "currentWeekType": None,
            "isSessionStarted": None,
            "sessionStartDate": None,
            "sessionEndDate": None,
            "examsSchedule": [],
            "educationalPracticeStartDate": None,
            "educationalPracticeEndDate": None,
            "holidaysStartDate": None,
            "holidaysEndDate": None
        }
    }
    get_object_or_404(Group, groupNumber=got_group_number)

    facultyName = Group.objects.filter(groupNumber=got_group_number).values('facultyChoice').get()['facultyChoice']
    course = Group.objects.filter(groupNumber=got_group_number).values('courseChoice').get()['courseChoice']

    sessionStartDate = Group.objects.filter(groupNumber=got_group_number).values('sessionStartDate').get()[
        'sessionStartDate']
    sessionEndDate = Group.objects.filter(groupNumber=got_group_number).values('sessionEndDate').get()[
        'sessionEndDate']

    if sessionStartDate <= datetime.date.today() <= sessionEndDate:
        return_group_table_data['tables']['isSessionStarted'] = True
    else:
        return_group_table_data['tables']['isSessionStarted'] = False

    i = 0
    current_week = datetime.date.today().isocalendar()[2]
    if int(Group.objects.filter(groupNumber=got_group_number).values('groupWeekTypeChoice').get()[
               'groupWeekTypeChoice']) == 1:
        tmp = int(Group.objects.filter(groupNumber=got_group_number).values('groupWeekTypeChoice').get()[
                      'groupWeekTypeChoice'])
        while i < current_week:
            tmp = 1 - tmp
            return_group_table_data['tables']['currentWeekType'] = tmp + 1
            i += 1
    else:
        tmp = int(Group.objects.filter(groupNumber=got_group_number).values('groupWeekTypeChoice').get()[
                      'groupWeekTypeChoice'])
        while i < current_week:
            tmp = 1 - tmp
            return_group_table_data['tables']['currentWeekType'] = tmp - 1
            i += 1

    groupId = Group.objects.get(groupNumber=got_group_number).id
    groupTable = GroupLesson.objects.filter(groupIdConnector=groupId).values()

    tables_values = ['semesterStartDate', 'semesterEndDate',
                     'educationalPracticeStartDate', 'educationalPracticeEndDate',
                     'holidaysStartDate', 'holidaysEndDate', 'sessionStartDate', 'sessionEndDate']

    for i in tables_values:
        return_group_table_data['tables'][i] = Group.objects.filter(groupNumber=got_group_number).values(i).get()[
            i]
        if Group.objects.filter(groupNumber=got_group_number).values('groupWeekTypeChoice').get()[
                'groupWeekTypeChoice'] != '-1':
            return_group_table_data['tables']['isWeekTypeNeeded'] = False
        else:
            return_group_table_data['tables']['isWeekTypeNeeded'] = True

    return_group_table_data['studentGroup']['groupNumber'] = got_group_number
    return_group_table_data['studentGroup']['facultyName'] = facultyName
    return_group_table_data['studentGroup']['course'] = course

    for i in range(len(groupTable)):
        inner_lesson_list = {
            "subject": groupTable[i]['subject'],
            "subjectType": groupTable[i]['lessonTypeChoice'],
            "weekType": groupTable[i]['weekTypeChoice'],
            "auditory": groupTable[i]['auditory'],
            "startLessonTime": groupTable[i]['startLessonTime'],
            "endLessonTime": groupTable[i]['endLessonTime'],
            "employee": {
                "fullName": groupTable[i]['employeeFullName'],
                # "fio": None
            },
            "note": groupTable[i]['note']
        }
        return_group_table_data['tables']['weekDay'][groupTable[i]['weekDayChoices']]['lessonList'] \
            .append(inner_lesson_list)

    return JsonResponse(return_group_table_data)


def get_group_list(request):
    return_data = {
        "groupsList": []
    }
    test_ = Group.objects.filter().values('groupNumber')
    for i in range(len(test_)):
        group_num = Group.objects.filter().values('groupNumber')[i].get('groupNumber')
        return_data['groupsList'].append(group_num)
    return JsonResponse(return_data)
    # return HttpResponse(return_data)
