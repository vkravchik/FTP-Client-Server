from django.db import models


class Connection(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=60)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    secure = models.BooleanField(null=False)

    def __str__(self):
        return self.host