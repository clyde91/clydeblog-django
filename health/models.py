from django.db import models


class MyHealth(models.Model):
    weight = models.DecimalField(decimal_places=1, max_digits=3, verbose_name="体重",)
    record_date = models.DateTimeField(auto_now_add=True, verbose_name="记录日期")

    class Meta:
        verbose_name_plural = "健康"
        ordering = ['-record_date']


class Run(models.Model):
    distance = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="距离",)
    time = models.DecimalField(decimal_places=2, max_digits=4, verbose_name="时间",)
    record_date = models.DateTimeField(auto_now_add=True, verbose_name="记录日期")

    class Meta:
        verbose_name_plural = "跑步"
        ordering = ['-record_date']
