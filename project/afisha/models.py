import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.IntegerField()
    is_checked = models.BooleanField(default=False) #event is checked by admin and ready for publication
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=3) <= self.pub_date <= now

class Comment(models.Model):
    comment_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
