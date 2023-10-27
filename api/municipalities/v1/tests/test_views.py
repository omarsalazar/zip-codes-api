from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory

from api.users.test.factories import UserFactory
from ..models import MunicipalityModel
from .factories import MunicipalityFactory

fake = Faker()


class TestMunicipalityCreateTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        self.url = reverse('municipalitymodel-list')
        self.municipality_data = factory.build(dict, FACTORY_CLASS=MunicipalityFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.municipality_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        municipality = MunicipalityModel.objects.get(pk=response.data.get('id'))
        eq_(municipality.name, self.municipality_data.get('name'))


class TestMunicipalityDetailTestCase(APITestCase):


    def setUp(self):
        self.user = UserFactory()
        self.municipality_data = MunicipalityFactory(name="test")
        self.url = reverse('municipalitymodel-detail', kwargs={'pk': self.municipality_data.id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_given_municipality(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_put_request_updates_a_municipality(self):
        new_name = "Test name"
        payload = {'name': new_name}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        municipality = MunicipalityModel.objects.get(pk=self.municipality_data.id)
        eq_(municipality.name, new_name)
