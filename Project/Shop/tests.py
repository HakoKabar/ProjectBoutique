
from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from .models import Category


class TestCategory(APITestCase):
    url=reverse_lazy('c_ategory-list')

    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test1_list(self):
        category=Category.objects.create(name='casquette',active=True)
        

        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

        expected = [
            {
                'id': category.pk,
                'date_created':self.format_datetime(category.date_created),
                'date_updated':self.format_datetime(category.date_updated),
                'name':category.name,
                
            }
        ]
        self.assertEqual(expected,response.json())
        

    def test2_list(self):
        category=Category.objects.create(name='casquette',active=False)
        

        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

        expected = [
            {
                'id': category.pk,
                'date_created':self.format_datetime(category.date_created),
                'date_updated':self.format_datetime(category.date_updated),
                'name':category.name,
                
            }
        ]
        self.assertEqual(expected,response.json())
        
