from django.db import models
from users.models import User


# Create your models here.




class Neighbourhood(models.Model):
    hood_name = models.CharField(verbose_name='Neighbourhood Name', max_length=100)
    hood_loc = models.CharField(verbose_name='Neighbourhood Location', max_length=100)
    description = models.TextField(null=True)
    hood_image = models.ImageField(upload_to = 'hood_images', null=True)
    contact_info = models.TextField(null=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    @classmethod
    def find_neighbourhood(cls, id):
        return cls.objects.get(pk=id)
    @classmethod
    def update_neighbourhood(cls, name, new_name):
        return cls.objects.filter(hood_name = name).update(hood_name = new_name)


    @property
    def occupants_count(self):
        return Neighbourhood.objects.all().count()



class Business(models.Model):
    biz_name = models.CharField(verbose_name='Business Name', max_length=100)
    user = models.ForeignKey(User, related_name='business', on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='business', on_delete=models.CASCADE, null=True)
    biz_email = models.EmailField(verbose_name='Business Email')


    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    @classmethod
    def find_business(cls, id):
        return cls.objects.get(pk=id)
    @classmethod
    def update_business(cls, name, new_name):
        return cls.objects.filter(biz_name = name).update(biz_name = new_name)


class Post(models.Model):
    title = models.CharField(max_length=100)
    post = models.TextField()
    post_image = models.ImageField(upload_to = 'post_images', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE, null=True)
