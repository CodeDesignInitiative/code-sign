from django.db import models


class Signature(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    signature = models.CharField(max_length=65536)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}  at {}".format(self.first_name, self.last_name, self.date)
