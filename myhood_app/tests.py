from django.test import TestCase
from django.contrib.auth.models import User

from myhood_app.models import Business, Neighbourhood

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'okunzo',email = 'okunzo2022@gmail.com')
        self.neighbourhood = Neighbourhood(hood_name = 'Ingo hood', hood_loc='Vihiga', description = 'Home away from home', admin = self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, Neighbourhood))

    def test_save_hood(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods)>0)

    def test_delete_hood(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods)<1)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User(username = 'okunzo',email = 'okunzo2022@gmail.com')
        self.neighbourhood = Neighbourhood(hood_name = 'Ingo hood', hood_loc='Vihiga', description = 'Home away from home', admin = self.user)
        self.business = Business(biz_name='General store', user=self.user, neighbourhood=self.neighbourhood, biz_email='store@gmail.com')
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        self.business.create_business()
        bizs = Business.objects.all()
        self.assertTrue(len(bizs)>0)

    def test_delete_business(self):
        self.user.save()
        self.neighbourhood.create_neighbourhood()
        self.neighbourhood.create_neighbourhood()
        self.business.create_business()
        self.business.delete_business()
        bizs = Business.objects.all()
        self.assertTrue(len(bizs)<1)