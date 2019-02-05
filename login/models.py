from django.db import models

# Create your models here.


class User(models.Model):


    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    #kami = models.CharField(max_length=255,default="未找到，请等待十分钟或联系卖家")
    kamiid = models.ForeignKey('Kami',on_delete=models.CASCADE,to_field='kamiid')
    #email = models.EmailField(unique=True)
    #sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class Kami(models.Model):

    kamiid = models.CharField(max_length=255,unique=True,)
    kamizhi =  models.CharField(max_length=255,default="未找到，请等待十分钟或联系卖家")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kamiid

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "卡密"
        verbose_name_plural = "卡密"


