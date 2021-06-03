from django.db import models

# Create your models here.
class Fruit (models.Model):
    name = models.CharField(u'nombre', default="", max_length=255)
    price = models.FloatField(u"precio unitario", default=0)
