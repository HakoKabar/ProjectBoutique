from django.http import response
from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from .models import Category


class TestCategory(APITestCase):
    url=reverse_lazy('c_ategory-list')

    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        category=Category.objects.create(name=4,active=True)
        Category.objects.create(name=5,active=False)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

        expected = [
            {
                'id': category.pk,
                'name':category.name,
                'date_created':self.format_datetime(category.date_created),
                'date_updated':self.format_datetime(category.date_updated)
            }
        ]
        self.assertEqual(response.json(),expected)
