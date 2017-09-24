from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

# РЕГИОНЫ СТРАНЫ
class Region(models.Model):
    """ Регион (область, край) """
    name = models.CharField(
        'Наименование республики/края/области/округа', max_length=80)

    def __str__(self):
        return self.name[:31]

    class Meta:
        ordering = ('id',)
        verbose_name = 'Республика / Край / Область / Округ'
        verbose_name_plural = 'Республики / Края / Области / Округа'

# МУНИЦИПАЛЬНЫЕ ОБРАЗОВАНИЯ ПО РЕГИОНАМ
class District(models.Model):
    """ Район (субъект) """
    region = models.ForeignKey(Region, related_name='district')
    kind = models.CharField(
        'Тип муниципального образования', 
        max_length=80)
    name = models.CharField(
        'Наименование муниципального образования', 
        max_length=80)
    okato = models.CharField(
        """Общероссийский классификатор объектов 
        административно-территориального деления""", 
        max_length=32)
    oktmo = models.CharField(
        """Общероссийский классификатор территорий муниципальных образований""", 
        max_length=32)

    def __str__(self):
        if 'район' in self.kind:
            return ' '.join([self.region.name, 
                             self.name, 
                             self.kind])
        else:
            return ' '.join([self.region.name, 
                             self.kind, 
                             self.name])

    class Meta:
        ordering = ('id',)
        verbose_name = 'Муниципальное образование'
        verbose_name_plural = 'Муниципальные образования'

# АБСТРАКТНЫЙ КЛАСС ФИЗЛИЦА
class Person(models.Model):
    """ Физическое лицо """
    first_name = models.CharField(
        'Имя', max_length=128)
    sur_name = models.CharField(
        'Отчество', max_length=256, blank=True)
    last_name = models.CharField(
        'Фамилия', max_length=128)
    birth_date = models.DateField(
        'Дата рождения', blank=True, null=True)
    no_phone = models.TextField(
        'Контактный телефон', blank=True)
    created = models.DateTimeField(
        'Дата и время внесения в базу', auto_now_add=True)
    modified = models.DateTimeField(
        'Дата и время изменения в базе', auto_now=True)

    def __str__(self):
        return ' '.join([self.last_name, 
                         self.first_name])

    def full_name(self):
        return ' '.join([self.last_name, 
                         self.first_name, 
                         self.sur_name])

    class Meta:
        abstract = True

# ОРГАНИЗАЦИЯ, ЮРЛИЦО
class Organization(models.Model):
    """ Организация """
    with_us = models.BooleanField('Загегистрирована ли организация', 
        default=False)
    group = models.ForeignKey(Group, default=1, 
        on_delete=models.CASCADE, related_name='organization')
    full_name = models.CharField(
        'Полное наименование', max_length=512)
    name = models.CharField(
        'Сокращённое наименование', max_length=80)
    inn = models.CharField(
        'ИНН', max_length=12)
    kpp = models.CharField(
        'КПП', max_length=12)
    district = models.ForeignKey(District, default=6, 
        help_text='Муниципальное образование', related_name='organization')
    legal_address = models.TextField(
        'Юридический адрес')
    actual_address = models.TextField(
        'Фактический адрес')
    no_phone = models.TextField(
        'Телефон бухгалтерии')
    email = models.EmailField(
        'e-mail')
    no_users = models.PositiveSmallIntegerField(
        'Заявляемое количество пользователей', default=1)
    created = models.DateTimeField(
        'Дата и время внесения в базу', auto_now_add=True)
    modified = models.DateTimeField(
        'Дата и время изменения в базе', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        permissions = (
            ('can_view', 'Могут видеть доступные организации'),
            ('can_change', 'Могут менять данные об организации'),
        )

# ПРАВОМОЧНЫЙ ПРЕДСТАВИТЕЛЬ ОРГАНИЗАЦИИ
class AuthorizedPerson(Person):
    """ Подписывающее договор лицо """
    organization = models.ForeignKey(Organization, 
        related_name='authorized_person')

    class Meta:
        verbose_name = 'Подписывающее договор лицо'
        verbose_name_plural = 'Подписывающее договора лица'

# КОНТАКТНОЕ ЛИЦО - АДМИН ОРГАНИЗАЦИИ
class AdminOfOrganization(Person):
    """ Контактное лицо - администратор организации """
    organization = models.ForeignKey(Organization, 
        related_name='contact_person')

    class Meta:
        verbose_name = 'Контактный администратор'
        verbose_name_plural = 'Контактные администраторы'

# ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ ОРГАНИЗАЦИИ
class Profile(models.Model):
    """ Профиль клиента с аватарками и IP """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
        related_name='profile')
    avatar = models.ImageField(
        upload_to='images/users', verbose_name='Изображение')
    ip = models.GenericIPAddressField(
        verbose_name='IP пользователя')
    organization = models.ForeignKey(Organization, 
        related_name='profile')

    def get_user_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    class Meta:
        verbose_name = 'Профиль Пользователя'
        verbose_name_plural = 'Профили Пользователей'
