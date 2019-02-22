from django.db import models
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:model-form', kwargs={'pk': self.pk})
