from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    title = models.CharField(max_length=64,help_text='snack title',default='SweetSnack')
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField(default='description')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('snacks_detail', args=[self.id])