from django.db import models


class HPBXServer(models.Model):
    short_name = models.CharField(max_length=255)
    api_fqdn = models.CharField(max_length=255)
    calls_fqdn = models.CharField(max_length=255)

    def __str__(self):
        return self.short_name

