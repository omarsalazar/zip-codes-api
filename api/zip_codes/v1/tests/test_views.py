from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from faker import Faker
import factory

from api.federal_entities.v1.tests.factories import FederalEntityFactory
from api.municipalities.v1.tests.factories import MunicipalityFactory
from api.users.test.factories import UserFactory
from ..models import ZipCodeModel
from .factories import ZipCodeFactory

fake = Faker()


class TestZipCodeCreateTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        self.url = reverse('zipcode-list')
        self.zip_code_data = factory.build(dict, FACTORY_CLASS=ZipCodeFactory)
        # self.zip_code_data.municipality = MunicipalityFactory()
        # self.zip_code_data.federal_entity = FederalEntityFactory()

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_post_request_with_valid_data_succeeds(self):
    #     response = self.client.post(self.url, self.zip_code_data, format="json")
    #     eq_(response.status_code, status.HTTP_201_CREATED)

        # zip_code_data = ZipCodeModel.objects.get(pk=response.data.get('id'))
        # eq_(zip_code_data.zip_code, self.zip_code_data.get('zip_code'))

# class TestZipCodeDetailTestCase(APITestCase):
#     """
#     Tests /users detail operations.
#     """
#
#     def setUp(self):
#         self.user = UserFactory()
#         self.zip_code_data = ZipCodeFactory(zip_code="56430")
#         # self.url = reverse('zipcodemodel-list', kwargs={'pk': self.zip_code_data.id})
#         self.url = reverse('zipcodemodel-list')
#         self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
#
#     def test_get_request_returns_a_given_zip_code(self):
#         response = self.client.get(self.url)
#         eq_(response.status_code, status.HTTP_200_OK)

# def test_put_request_updates_a_zip_code(self):
#     new_zip_code = "15900"
#     payload = {'zip_code': new_zip_code}
#     response = self.client.patch(self.url, payload)
#     eq_(response.status_code, status.HTTP_200_OK)
#
#     zip_code_data = ZipCodeModel.objects.get(pk=self.zip_code_data.id)
#     eq_(zip_code_data.zip_code, new_zip_code)
