from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    added_on = models.DateTimeField(_("Date"), default=datetime.datetime.now)
    prof_image = models.ImageField(upload_to='profile_image', blank = True)

    def __str__(self):
        return '%s' % (self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
