from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from rest_framework import serializers

from app.models import Author, Country, Books


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author details"""

    class Meta:
        """docstring for Meta"""
        model = Author
        exclude = ('created', 'updated', 'mode', 'id')


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for Country details"""

    class Meta:
        """docstring for Meta"""
        model = Country
        exclude = ('created', 'updated', 'mode', 'id')


class BooksSerializer(serializers.ModelSerializer):
    """Serializer for Books details"""

    authors = AuthorSerializer(many=True,)
    country = CountrySerializer()

    class Meta:
        """docstring for Meta"""
        model = Books
        exclude = ('created', 'updated', 'mode',)


class BooksUpdateSerializer(serializers.ModelSerializer):
    """Serializer for Books details"""

    class Meta:
        """docstring for Meta"""
        model = Books
        exclude = ('created', 'updated', 'mode')



