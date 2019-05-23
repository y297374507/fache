from django.db import models
from django.urls import reverse
# Create your models here.


class Fachekehu(models.Model):
    name = models.CharField('发车客户', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '发车客户表'
        verbose_name_plural = '发车客户表'


class Daozhan(models.Model):
    name = models.CharField('到站', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '到站表'
        verbose_name_plural = '到站表'

    # def get_absolute_url(self):
    #     return reverse('daozhan_detail', args=[self.id])


class Huowu(models.Model):
    name = models.CharField('货物种类', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '货物种类表'
        verbose_name_plural = '货物种类表'

class Baozhuang(models.Model):
    name = models.CharField('包装类型', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '包装类型表'
        verbose_name_plural = '包装类型表'

class Guige(models.Model):
    name = models.CharField('货物规格', max_length=50)
    value = models.FloatField('计量数值')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '货物规格表'
        verbose_name_plural = '货物规格表'


class Fache(models.Model):
    date = models.DateField('计划装车日期')
    daozhan = models.ForeignKey(Daozhan, on_delete=models.CASCADE, verbose_name='到站')
    huowu = models.ForeignKey(Huowu, on_delete=models.CASCADE, verbose_name='货物')
    # guige = models.ForeignKey(Guige, on_delete=models.CASCADE, verbose_name='规格')
    # baozhuang = models.ForeignKey(Baozhuang, on_delete=models.CASCADE, verbose_name='包装')
    fachekehu = models.ForeignKey(Fachekehu, on_delete=models.CASCADE, verbose_name='发车客户')

    def __str__(self):
        return '{}{}'.format(self.fachekehu, self.daozhan)

    class Meta:
        verbose_name = '发车计划表'
        verbose_name_plural = '发车计划表'
        ordering = ('-date', )



class Jisuan(models.Model):
    number = models.ForeignKey(Fache, on_delete=models.CASCADE, verbose_name='编号')
    guige = models.ForeignKey(Guige, on_delete=models.CASCADE, verbose_name='规格')
    baozhuang = models.ForeignKey(Baozhuang, on_delete=models.CASCADE, verbose_name='包装')
    jianshu = models.PositiveIntegerField('件数')
    # zhongliang = models.FloatField()

    def __str__(self):
        return '{}{}'.format(self.guige, self.jianshu)


    def sum_zhongliang(self):
        self.value = Guige.objects.get(name=self.guige).value
        return self.jianshu * self.value

    class Meta:
        verbose_name = '发车数量表'
        verbose_name_plural = '发车数量表'



