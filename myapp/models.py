from django.db import models
from django.conf import settings

# Create your models here.
class Organizer(models.Model):
    def __str__(self):
        return self.name
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='organizer')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)


class Event(models.Model):

    def __str__(self):
        return self.title
    organizer = models.ForeignKey(Organizer,on_delete=models.CASCADE,related_name='events')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    price = models.IntegerField()
    venue = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    banner = models.ImageField(upload_to='event_banners/',blank=True,null=False)