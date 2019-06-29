import json

from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from mstakxapp.utils.customeapiresponse import ResponseModelViewSet, ResponseInfo
from app.serializers import BooksSerializer, CountrySerializer, AuthorSerializer, BooksUpdateSerializer
from app.models import Author, Country, Books
from rest_framework.views import APIView
import requests


class BooksViewSet(ResponseModelViewSet):
    queryset = Books.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return BooksUpdateSerializer
        else:
            return BooksSerializer


class CountryViewSet(ResponseModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


class AuthorViewSet(ResponseModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)


class ExternalBooksListView(APIView):

    def get(self, request):
        url = 'https://www.anapioficeandfire.com/api/books'
        if request.GET.get('name'):
            url = url + '?name={0}'.format(request.GET.get('name'))
        resp = requests.get(url)
        results = json.loads(resp.content)
        response_format = ResponseInfo().response
        if results:
            list_value = []
            for each in results:
                required_dict = dict()
                required_dict['name'] = each.get('name')
                required_dict['isbn'] = each.get('isbn')
                required_dict['authors'] = each.get('authors')
                required_dict['number_of_pages'] = each.get('number_of_pages')
                required_dict['publisher'] = each.get('publisher')
                required_dict['country'] = each.get('country')
                required_dict['release_date'] = each.get('release_date')
                list_value.append(required_dict)
            response_format['data'] = list_value
            return Response(response_format)
        else:
            return Response(response_format)


