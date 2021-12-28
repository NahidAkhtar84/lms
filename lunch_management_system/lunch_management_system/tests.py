from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from employee.models.user import User

from faker import Faker
fake = Faker()

class WithAuthUser(APITestCase):

    def setUp(self):
        email = fake.email()
        username=fake.name()
        password = "12345678na"
        self.user = User.objects.create_user(
            username=username,
            password=password
        )

        self.refresh = RefreshToken.for_user(self.user)
        self.token = str(self.refresh.access_token)
        self.api_authentication()

        self.user.is_staff = True
        self.user.is_active = True
        self.user.save()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
