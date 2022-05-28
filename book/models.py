from django.db import models
from django.contrib.auth.models import User

class BookJournalBase(models.Model): #Model abstract
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateField(blank=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name

class Books(BookJournalBase):
    num_pages = models.IntegerField(default=1)
    genre = models.TextField(blank=True)
    class Meta(BookJournalBase.Meta): #Model inheritance
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.name

class Journal(BookJournalBase):
    publisher = models.TextField(blank=True)
    class Meta(BookJournalBase.Meta): #Model inheritance
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'

    def __str__(self):
        return self.name
