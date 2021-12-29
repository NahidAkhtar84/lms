import json
from django.urls import reverse
from lunch_management_system.tests import WithAuthUser

from rest_framework.test import force_authenticate

from faker import Faker
fake = Faker()


class EmployeesTestCase(WithAuthUser):
    url = reverse('employee:employee')
    url_detail=reverse('employee:employee-detail')

    def setUp(self):
        super().setUp()

        self.data = {
            "email": fake.email(),
            "name": fake.name(),
            "username": fake.name(),
            "password": "12345678na"
        }
        

    def test_create_employee_post_201(self):
        response = self.client.post(self.url, self.data, format="json")
        force_authenticate(response, user=self.user)
        self.assertEqual(201, response.status_code)
        return response.data

    def test_employee_list_get_200(self):
        self.test_create_employee_post_201()
        response = self.client.get(self.url)
        force_authenticate(response, user=self.user)
        self.assertEqual(200, response.status_code)
