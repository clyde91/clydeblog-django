from django.db import models 
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, null=True, blank=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to="user", null=True, blank=True, verbose_name='头像')

    def __str__(self):
        return '<个人信息: %s for %s>' % (self.nickname, self.user.username)

    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '/media/user/guest.jpg'
