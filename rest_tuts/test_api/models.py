from datetime import datetime
from pyexpat import model
from django.db import models

# Create your models here.


class Shows(models.Model):
    s_id = models.AutoField(primary_key=True, default=1)
    m_id = models.IntegerField()
    price = models.IntegerField()
    capacity = models.BooleanField(default=True)

    def __str__(self):
        return str(self.s_id)



class Booked(models.Model):
    b_id = models.AutoField(primary_key=True, default=1001)
    s_id = models.ForeignKey(Shows, on_delete=models.CASCADE)
    b_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.b_id)

