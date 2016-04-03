from django.db import models

# Create your models here.
class Quotes(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    def __str__(self):
        return ' '.join([
            self.quote,
            self.author,
            ])
