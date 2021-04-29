from django.db import models
from datetime import datetime


class Group(models.Model):
    group_number = models.CharField('Номер группы', max_length=10)

    lech = 'Лечебный'
    med_prof = 'Медико-профилактический'
    ped = 'Педиатрический'
    stom = 'Стоматологический'
    voen_med = 'Военно-медицинский'
    inostr = 'Иностранных учащихся'
    farm = 'Фармацевтический'
    profor = 'Профориентации и довузовской подготовки'
    fac_pov_kv = 'Факультет повышения квалификации и переподготовки кадров'
    faculties_choices = [
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
    faculty_choice = models.CharField(
        'Факультет',
        max_length=75,
        choices=faculties_choices
    )

    course_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]
    course_choice = models.CharField(
        'Курс',
        max_length=10,
        choices=course_choices,
    )

    semester_start_date = models.DateField(verbose_name='Начало семестра')
    semester_end_date = models.DateField(verbose_name='Конец семестра')
    group_week_type_choices = [
        ('1', 'Нечетная'),
        ('2', 'Четная'),
        (None, 'Не учитывать'),
    ]
    group_week_type_choice = models.CharField(
        'Тип первой учебной недели',
        default=None,
        choices=group_week_type_choices,
        max_length=1,
    )
    # is_week_type_needed = models.BooleanField(verbose_name='Учитывается ли четность недели?')

    session_start_date = models.DateField(verbose_name='Начало экзаменов')
    session_end_date = models.DateField(verbose_name='Конец экзаменов')

    educational_practice_start_date = models.DateField(verbose_name='Начало учебной практики')
    educational_practice_end_date = models.DateField(verbose_name='Конец учебной практики')

    holidays_start_date = models.DateField(verbose_name='Начало каникул')
    holidays_end_date = models.DateField(verbose_name='Конец каникул')

    def __str__(self):
        return self.group_number

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'информацию группы'


class GroupLesson(models.Model):
    group_id_connector = models.ForeignKey(Group, on_delete=models.CASCADE)

    week_day_choices = [
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресение', 'Воскресение'),
    ]
    week_day_choice = models.CharField(
        'День недели',
        choices=week_day_choices,
        max_length=100
    )

    subject = models.CharField(
        'Дисциплина',
        max_length=100,
    )

    lesson_type_choices = [
        ('ЛК', 'Лекция'),
        ('ПЗ', 'Практическое'),
        (' ', 'Не указывать')
    ]
    lesson_type_choice = models.CharField(
        'Тип занятия',
        choices=lesson_type_choices,
        max_length=100
    )

    week_type_choices = [
        ('0', 'Каждая'),
        ('1', 'Нечетная'),
        ('2', 'Четная'),
        ('-1', 'Иная')
    ]
    week_type_choice = models.CharField(
        'Тип недели',
        choices=week_type_choices,
        max_length=100,
    )

    special_days = models.CharField('Отдельные дни', max_length=100, blank=True,
                                    help_text='Если занятие проводится по отдельным датам. '
                                              'Например, <b>18.09 15.10 16.11</b>')
    auditory = models.CharField('Аудитория', max_length=10, blank=True)
    start_lesson_time = models.TimeField('Время начала пары')
    end_lesson_time = models.TimeField('Время конца пары')
    employee_full_name = models.CharField('Преподаватель (ФИО полностью)', max_length=100, blank=True)
    note = models.CharField('Примечание', max_length=100, blank=True)

    class Meta:
        verbose_name_plural = 'Пары'
        verbose_name = 'Пара'

    def __str__(self):
        return self.subject


class SemesterOptions(models.Model):

    # semester_start = models.DateField('Начало семестра')

    # server_week_type_choices = [
    #     ('1', 'Нечетная'),
    #     ('2', 'Четная'),
    # ]
    # server_week_type_choice = models.CharField(
    #     'Тип текущей учебной недели',
    #     default='1',
    #     choices=server_week_type_choices,
    #     max_length=1,
    #     help_text='Тип недели обязательное значение'
    # )

    # semester_end = models.DateField('Конец семестра')

    def __str__(self):
        return 'Настройки семестра'

    class Meta:
        verbose_name_plural = 'Настройки семестра'
        verbose_name = 'Настройки семестра'
