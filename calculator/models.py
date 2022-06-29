from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование банка')
    term_min = models.PositiveIntegerField(verbose_name='Срок ипотеки, ОТ')
    term_max = models.PositiveIntegerField(verbose_name='Срок ипотеки, ДО')
    rate_min = models.PositiveSmallIntegerField(verbose_name='Ставка, ОТ')
    rate_max = models.PositiveSmallIntegerField(verbose_name='Ставка, ДО')
    payment_min = models.PositiveIntegerField(verbose_name='Сумма кредита, ОТ')
    payment_max = models.PositiveIntegerField(verbose_name='Сумма кредита, ДО')

    def __str__(self):
        return self.name


'''''''''
Можно добавить:
Цель ипотеки
подтверждение дохода
Обеспечение
Возраст заемщика и т.д.
Но для данных целей данных полей достаточно

'''''''''