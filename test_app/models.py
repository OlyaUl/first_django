from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    year = models.DateField()
    description = models.CharField(max_length=1000)
    authors = models.ManyToManyField('Author')
    category = models.ForeignKey('Caterogy', on_delete=models.CASCADE)
    # image = models.ImageField()
    # prev = models.ImageField()

    def __str__(self):
        return '{0} {1}'.format(self.authors, self.category)


class Caterogy(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)


class Author(models.Model):
    name = models.CharField(max_length=30)
    date_bir = models.DateField()
    bio = models.CharField(max_length=1000)

