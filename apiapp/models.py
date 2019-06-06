from django.db import models
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    #id = models.IntegerField(primary_key=True, null=False)
    fname = models.CharField(max_length = 100)
    sname = models.CharField(max_length = 100)
    sex = models.CharField(max_length = 100)
    amount = models.CharField(max_length = 100)
    date_deposited = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.fname
