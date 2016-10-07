from django.db import models

class Main(models.Model):
    region = models.CharField(max_length=100, verbose_name=u'Группа')
    country = models.CharField(max_length=100, verbose_name=u'Страна')
    value = models.FloatField(verbose_name=u'Значение')

    def __str__(self):
        return self.region

