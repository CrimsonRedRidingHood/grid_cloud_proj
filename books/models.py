from django.db import models

# Create your models here.

class Book(models.Model):
    genre = models.CharField(max_length=40)
    book_name = models.CharField(max_length=200)
    pub_year = models.IntegerField()
    def __str__(self):
        return self.book_name