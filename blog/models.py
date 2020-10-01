from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,validators=[MinLengthValidator(8)])
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    body = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args = [str(self.id)])