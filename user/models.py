from django.db import models 
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="extand")
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name='昵称')
    avatar = models.ImageField(null=True, blank=True,verbose_name='头像')

    def __str__(self):
        return '<个人信息: %s for %s>' % (self.nickname, self.user.username)
