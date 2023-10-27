from django.urls import reverse
from nose.tools import eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory

from api.users.test.factories import UserFactory
from ..models import FederalEntityModel
from .factories import FederalEntityFactory

fake = Faker()


class TestFederalEntityCreateTestCase(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')
        self.url = reverse('federalentitymodel-list')
        self.federal_entity_data = factory.build(dict, FACTORY_CLASS=FederalEntityFactory)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.federal_entity_data)
        eq_(response.status_code, status.HTTP_201_CREATED)

        federal_entity_data = FederalEntityModel.objects.get(pk=response.data.get('id'))
        eq_(federal_entity_data.name, self.federal_entity_data.get('name'))


class TestFederalEntityDetailTestCase(APITestCase):


    def setUp(self):
        self.user = UserFactory()
        self.federal_entity_data = FederalEntityFactory(name="test")
        self.url = reverse('federalentitymodel-detail', kwargs={'pk': self.federal_entity_data.id})
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user.auth_token}')

    def test_get_request_returns_a_given_federal_entity(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_put_request_updates_a_federal_entity(self):
        new_name = "Test name"
        payload = {'name': new_name}
        response = self.client.patch(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        federal_entity_data = FederalEntityModel.objects.get(pk=self.federal_entity_data.id)
        eq_(federal_entity_data.name, new_name)
