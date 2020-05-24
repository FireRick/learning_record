from django.db import models

class Item(models.Model):
    """ learning item """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.CharField(max_length=1000, verbose_name='Description')
    record_sum = models.IntegerField()


class Record(models.Model):
    """ learning record """
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()  # time of learning
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # brief intro of what you learned
    key_content = models.CharField(max_length=200, verbose_name='Key Content')
    description = models.CharField(max_length=1000, verbose_name='Description')
