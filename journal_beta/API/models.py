from django.db import models


class Group(models.Model):
    groupNumber = models.CharField('Номер группы', max_length=10)

    lech = 'Лечебный'
    med_prof = 'Медико-профилактический'
    ped = 'Педиатрический'
    stom = 'Стоматологический'
    voen_med = 'Военно-медицинский'
    inostr = 'Иностранных учащихся'
    farm = 'Фармацевтический'
    profor = 'Профориентации и довузовской подготовки'
    fac_pov_kv = 'Факультет повышения квалификации и переподготовки кадров'
    facultiesChoices = [
        (lech, 'Лечебный'),
        (med_prof, 'Медико-профилактический'),
        (ped, 'Педиатрический'),
        (stom, 'Стоматологический'),
        (voen_med, 'Военно-медицинский'),
        (inostr, 'Иностранных учащихся'),
        (farm, 'Фармацевтический'),
        (profor, 'Профориентации и довузовской подготовки'),
        (fac_pov_kv, 'Факультет повышения квалификации и переподготовки кадров'),
    ]
    facultyChoice = models.CharField(
        'Факультет',
        max_length=75,
        choices=facultiesChoices
    )

    courseChoices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]
    courseChoice = models.CharField(
        'Курс',
        max_length=10,
        choices=courseChoices,
    )

    semesterStartDate = models.DateField(verbose_name='Начало семестра')
    semesterEndDate = models.DateField(verbose_name='Конец семестра')

    groupWeekTypeChoices = [
        ('1', 'Нечетная'),
        ('2', 'Четная'),
        ('-1', 'Не учитывать'),
    ]
    groupWeekTypeChoice = models.CharField(
        'Тип первой учебной недели',
        default=None,
        choices=groupWeekTypeChoices,
        max_length=2,
    )

    sessionStartDate = models.DateField(verbose_name='Начало экзаменов')
    sessionEndDate = models.DateField(verbose_name='Конец экзаменов')

    educationalPracticeStartDate = models.DateField(verbose_name='Начало учебной практики')
    educationalPracticeEndDate = models.DateField(verbose_name='Конец учебной практики')

    holidaysStartDate = models.DateField(verbose_name='Начало каникул')
    holidaysEndDate = models.DateField(verbose_name='Конец каникул')

    def __str__(self):
        return self.groupNumber

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'информацию группы'


class GroupLesson(models.Model):
    groupIdConnector = models.ForeignKey(Group, on_delete=models.CASCADE)

    weekDayChoices = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресение', 'Воскресение'),
    ]
    weekDayChoices = models.CharField(
        'День недели',
        choices=weekDayChoices,
        max_length=100
    )

    subject = models.CharField(
        'Дисциплина',
        max_length=100,
    )

    lessonTypeChoices = [
        ('ЛК', 'Лекция'),
        ('ПЗ', 'Практическое'),
        (' ', 'Не указывать')
    ]
    lessonTypeChoice = models.CharField(
        'Тип занятия',
        choices=lessonTypeChoices,
        max_length=100
    )

    weekTypeChoices = [
        ('0', 'Каждая'),
        ('1', 'Нечетная'),
        ('2', 'Четная'),
        ('-1', 'Иная')
    ]
    weekTypeChoice = models.CharField(
        'Тип недели',
        choices=weekTypeChoices,
        max_length=100,
    )

    specialDays = models.CharField('Отдельные дни', max_length=100, blank=True,
                                   help_text='Если занятие проводится по отдельным датам. '
                                             'Например, <b>18.09 15.10 16.11</b>')
    auditory = models.CharField('Аудитория', max_length=10, blank=True)
    startLessonTime = models.TimeField('Время начала пары')
    endLessonTime = models.TimeField('Время конца пары')
    employeeFullName = models.CharField('Преподаватель (ФИО полностью)', max_length=100, blank=True)
    note = models.CharField('Примечание', max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Пары'
        verbose_name = 'Пара'

    def __str__(self):
        return self.subject
