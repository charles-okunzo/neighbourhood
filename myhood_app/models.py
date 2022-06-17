from django.db import models

from users.models import User

# Create your models here.


class Admin(models.Model):
    class Meta:
        model = User


class Neighbourhood(models.Model):
    hood_name = models.CharField(verbose_name='Neighbourhood Name', max_length=100)
    hood_loc = models.CharField(verbose_name='Neighbourhood Location', max_length=100)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)


    @property
    def occupants_count(self):
        return Neighbourhood.objects.all().count()



class Business(models.Model):
    biz_name = models.CharField(verbose_name='Business Name', max_length=100)
    user = models.ForeignKey(User, related_name='business', on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='business', on_delete=models.CASCADE)
    biz_email = models.EmailField(verbose_name='Business Email')