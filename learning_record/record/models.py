import datetime as dt

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

    @classmethod
    def get_specified_days_stat(cls, days):
        """ get stat of last specified days. """
        specified_days_ago = dt.date.today() - dt.timedelta(days=days)
        stat = []
        for item in Item.objects.all():
            count = cls.objects.filter(item=item).filter(time__gte=specified_days_ago).count()
            # drop item whoes count is 0;
            if count > 0:
                stat.append({
                    'name': item.name,
                    'count': count,
                })
        return stat

    @classmethod
    def get_today_stat(cls):
        """ get all records data of today. """
        return cls.get_specified_days_stat(0)

    @classmethod
    def get_seven_days_stat(cls):
        """ get all records data of last seven days. """
        return cls.get_specified_days_stat(7)

    @classmethod
    def get_this_year_stat(cls):
        """ get all records data of this year."""
        year = dt.date.today().year
        stat = []
        for item in Item.objects.all():
            count = cls.objects.filter(item=item).filter(time__year=year).count()
            # drop item whoes count is 0;
            if count > 0:
                stat.append({
                    'name': item.name,
                    'count': count,
                })
        return stat
