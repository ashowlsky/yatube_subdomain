from django.test import TestCase, Client
from .models import Post, User

class PageTest(TestCase):
    def SetUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='testemail@test.test', password='password')
    
    def testPageCodes(self):
        response = self.client.get("")
        self.assertEquals(response.status_code, 200, msg='status_code is supposed to be 200')

        response = self.client.get("/admin/")
        self.assertNotEquals(response.status_code, 200, msg='status_code is not supposed to be 200')


