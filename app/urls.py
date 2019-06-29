from django.urls import path, include, reverse_lazy, re_path
from django.contrib.auth.views import LoginView
from rest_framework.routers import DefaultRouter
from app.apis import BooksViewSet, CountryViewSet, AuthorViewSet, ExternalBooksListView

from mstakxapp.utils.apiurls import get_api_url

router = DefaultRouter(trailing_slash=False)
router.register(r'country', CountryViewSet)
router.register(r'books', BooksViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path(get_api_url(app_name=''), include(router.urls)),
    path('api/external-books', ExternalBooksListView.as_view(), name='external-books'),
]

