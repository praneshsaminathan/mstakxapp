import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from app.models import Country, Author


class CountryAPITests(APITestCase):
    def setUp(self):
        self.url = '/api/v1/country'
        self.client = APIClient()

    def test_create(self):
        self.data = {'name': "Test"}
        response = self.client.post(self.url, self.data, format='json')
        test_response = {'status_code': 201, 'status': 'success', 'data': {'name': 'Test'}}
        self.assertEqual((response.status_code, response.data), (status.HTTP_201_CREATED, test_response))


class AuthorAPITests(APITestCase):
    def setUp(self):
        self.url = '/api/v1/author'
        self.client = APIClient()

    def test_create(self):
        self.data = {'name': "Test Author"}
        response = self.client.post(self.url, self.data, format='json')
        test_response = {"status_code": 201, "status": "success", "data": {"name": "Test Author"}}
        self.assertEqual(
            (response.status_code, response.data),
            (status.HTTP_201_CREATED, test_response)
        )


class ExternalBooksAPITests(APITestCase):
    def setUp(self):
        self.url = '/api/external-books'
        self.client = APIClient()

    def test_external_api(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BooksAPITests(APITestCase):
    def setUp(self):
        self.url = '/api/v1/books'
        self.client = APIClient()
        self.country = Country.objects.create(name='test')
        self.author = Author.objects.create(name='test author')

    def test_create(self):
        self.data = {"name": "Test Author", "authors": [1], "country": 1, "isbn": "64568-356", "number_of_pages": 455,
                     "publisher": "Western World", "release_date": "1994-12-25"}
        self.data = json.dumps(self.data)
        response = self.client.post(self.url, self.data, content_type='application/json')
        test_response = {'status_code': 201, 'status': 'success',
                         'data': {'id': 1, 'name': 'Test Author', 'isbn': '64568-356', 'number_of_pages': 455,
                                  'publisher': 'Western World', 'release_date': '1994-12-25',
                                  'country': 1, 'authors': [1]}
                         }
        self.assertEqual((response.status_code, response.data), (status.HTTP_201_CREATED, test_response))

