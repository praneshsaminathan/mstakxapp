from django.db import models
from mstakxapp.utils import choices
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinValueValidator


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    mode = models.CharField(max_length=1, default='A', choices=choices.MODE)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=255, help_text=_('Author name'), verbose_name=_('Author name'))

    def __str__(self):
        return '{0}'.format(self.name)


class Country(BaseModel):
    name = models.CharField(max_length=255, help_text=_('Country'), verbose_name=_('Country'))

    def __str__(self):
        return '{0}'.format(self.name)


class Books(BaseModel):
    name = models.CharField(max_length=255, help_text=_('Book name'), verbose_name=_('Book name'))
    isbn = models.CharField(max_length=20, help_text=_('isbn'), verbose_name=_('isbn'), unique=True)
    authors = models.ManyToManyField(Author, help_text=_('authors'), verbose_name=_('authors'))
    number_of_pages = models.IntegerField(validators=[MinValueValidator(0)],
                                          help_text=_('Number of Pages'), verbose_name=_('Number of Pages'))
    publisher = models.CharField(max_length=255, help_text=_('Publisher'), verbose_name=_('Publisher'))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, help_text=_('Country'), verbose_name=_('Country'))
    release_date = models.DateField(help_text=_('Release Date'), verbose_name=_('Release Date'))

    def __str__(self):
        return '{0}'.format(self.name)

