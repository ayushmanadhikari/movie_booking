from datetime import datetime
from django.db import models



class movie(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=100)

    def __str__(self):
        return self.m_name



class Shows(models.Model):
    s_id = models.AutoField(primary_key=True)
    m_id = models.ForeignKey(movie, on_delete=models.CASCADE)
    price = models.IntegerField()
    capacity = models.BooleanField(default=True)

    def __str__(self):
        return str(self.s_id)



class Booked(models.Model):
    b_id = models.AutoField(primary_key=True)
    s_id = models.ForeignKey(Shows, on_delete=models.CASCADE)
    b_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.b_id)

