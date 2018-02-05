from django.db import models
from django.utils.html import format_html


class Signature(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    signature = models.CharField(max_length=8192)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
