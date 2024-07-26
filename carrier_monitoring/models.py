from django.db import models
from servers.models import HPBXServer


class CarrierMonitoring(models.Model):
    name = models.CharField(max_length=255)
    carrier = models.CharField(max_length=255)
    mon_server = models.CharField(max_length=255, db_index=True)
    last_check = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)
    alert = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CarrierMonUser(models.Model):
    carrier_monitoring = models.ForeignKey(CarrierMonitoring, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    hpbx_server = models.ForeignKey(HPBXServer, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    hp_org_id = models.CharField(max_length=20)
    device_id = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)

    class Meta:
        unique_together = ('carrier_monitoring', 'user_name')

    def __str__(self):
        return str(self.carrier_monitoring)+"_"+str(self.user_name)


