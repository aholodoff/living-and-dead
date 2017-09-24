from django.db import models
from django.conf import settings
from client.models import Region, District, AuthorizedPerson, \
                          AdminOfOrganization, Organization, Profile
from catalog.models import Cemetery, Structure, Work

# АБСТРАКТНЫЙ КЛАСС ФИЗЛИЦА
class Person(models.Model):
    """ Физическое лицо """
    first_name = models.CharField('Имя', max_length=128)
    sur_name   = models.CharField('Отчество', max_length=256, blank=True)
    last_name  = models.CharField('Фамилия', max_length=128)
    no_phone   = models.TextField('Контактный телефон', blank=True)
    birth_date = models.DateField('Дата рождения', blank=True, null=True)
    created    = models.DateTimeField('Дата и время внесения в базу', auto_now_add=True)
    modified   = models.DateTimeField('Дата и время изменения в базе', auto_now=True)

    def __str__(self):
        return '{fn}.{sn}.{ln}'.format(self.first_name[:1], 
                                       self.sur_name[:1], 
                                       self.last_name)

    def full_name(self):
        return ' '.join([self.last_name, 
                         self.first_name, 
                         self.sur_name])

    class Meta:
        abstract = True


class Burial(models.Model):
    """ Захоронение """
    NAME_CHOICES = (
        ('S', 'Одиночное'),
        ('R', 'Родственное'),
        ('F', 'Cемейное'),
        ('W', 'Воинское'),
        ('H', 'Почетное'))
    OPTION_CHOICES = (
        ('P', 'настоящее'),
        ('F', 'будующее'))
    name   = models.CharField('Вид захоронения', max_length=1, choices=NAME_CHOICES, default='R')
    option = models.CharField('Тип захоронения', max_length=1, choices=OPTION_CHOICES, default='P')
    info   = models.TextField('Примечание', blank=True)

    def __str__(self):
        return ' '.join([self.get_name_display(), 
                         self.get_option_display()])

    class Meta:
        verbose_name = 'Захоронение'
        verbose_name_plural = 'Захоронения'


class Declarant(Person):
    """ Подающее заявление лицо """
    class Meta:
        verbose_name = 'Заявитель'
        verbose_name_plural = 'Заявители'


class IdDocument(models.Model):
    """ Удостоверяющий личность документ """
    person  = models.ForeignKey(Declarant, related_name='id_document')
    kind    = models.CharField('Паспорт', max_length=64)
    series  = models.CharField('Серия', max_length=8)
    number  = models.CharField('Номер', max_length=16)
    address = models.CharField('Адрес регистрации по месту жительства', 
                               max_length=512, blank=True)
    issued_by = models.CharField('Кем выдан', 
                               max_length=512, blank=True)

    def __str__(self):
        return ''.join([self.person, self.kind])


class DeadMen(Person):
    """ Покойный """
    declarant     = models.ForeignKey(Declarant, related_name='dead_men')
    date_of_death = models.DateField('Дата смерти умершего')
    relation      = models.CharField('Степень родства по отношению к заявителю', 
                                     max_length=64, default='Мать')

    def __str__(self):
        return self.full_name()

    class Meta:
        verbose_name = 'Покойный'
        verbose_name_plural = 'Покойные'


class DeathCertificate(models.Model):
    """ Свидетельство о смерти """
    person  = models.ForeignKey(DeadMen, related_name='certificate')
    series  = models.CharField('Серия', max_length=8, blank=True)
    number  = models.CharField('Номер', max_length=16, blank=True)
    address = models.CharField('Адрес регистрации по месту жительства', 
                               max_length=512, blank=True)
    issued_by = models.CharField('Кем выдан', 
                               max_length=512, blank=True)

    def __str__(self):
        return ''.join([self.person, self.kind])


    class Meta:
        verbose_name = 'Св-во о смерти'
        verbose_name_plural = 'Св-ва о смерти'


class Place(models.Model):
    """ Участок захоронения """
    cemetery   = models.ForeignKey(Cemetery, related_name='place')
    dead_man    = models.ForeignKey(DeadMen, related_name='place')
    name         = models.CharField('Название участка', max_length=128)
    sector_number = models.CharField('Номер сектора', max_length=128)
    row_number    = models.CharField('Номер ряда', max_length=128)
    burial_number = models.CharField('Номер могилы', max_length=128)
    burial_resp   = models.CharField('ФИО ответственного за захоронение', 
                                   max_length=512)

    def __str__(self):
        return ''.join([self.dead_man.full_name, self.name])

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'


class BaseForm(models.Model):
    """ Основа форм """
    STATUS_CHOICES = (
        (1, 'В работе'),
        (2, 'Выдано'),
        (3, 'Отменено'))
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='base_form')
    status = models.PositiveSmallIntegerField('Статус обработки заявления', default=1)
    created = models.DateTimeField('Дата и время внесения в базу', auto_now_add=True)
    modified = models.DateTimeField('Дата и время изменения в базе', auto_now=True)

    class Meta:
        abstract = True


class FormNo1(BaseForm):
    """
    Заявление на предоставление места/ниши в стене скорби 
    для ... захоронения на кладбище ... для погребения ...
    """
    place  = models.OneToOneField(Place, related_name='formNo1')
    burial = models.ForeignKey(Burial, default=3, related_name='formNo1')
    responsible_for_burial = models.CharField('ФИО ответственного за захоронение', max_length=512, blank=True)
    responsible_for_burial_is_declarant = models.BooleanField('Является заявителем', default=True)

    def __str__(self):
        return self.dead_men.full_name()

    class Meta:
        verbose_name = 'Форма №1'
        verbose_name_plural = 'Формы №1'


class AdditionalDocument(models.Model):
    """ Дополнительный документ """
    form = models.ForeignKey(FormNo1)
    name = models.CharField('Наименование документа', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дополнительный документ'
        verbose_name_plural = 'Дополнительные документы'
