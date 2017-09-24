from django.db import models


class Cemetery(models.Model):
    """ Кладбище """
    name = models.CharField('Наименование кладбища', max_length=512)
    address = models.CharField('Адрес', max_length=512)
    info = models.TextField('Примечание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кладбище'
        verbose_name_plural = 'Кладбища'


class Structure(models.Model):
    """ Вид сооружения
    1 Надгробие
    2 Ограда 
    """
    name = models.CharField('Вид сооружения', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид сооружения'
        verbose_name_plural = 'Виды сооружений'


class Work(models.Model):
    """ Вид работы на участке захоронения """
    name = models.CharField('Вид работы на участке захоронения', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'
