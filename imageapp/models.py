from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.book_name

