from django.db import models

class ButtonClickStat(models.Model):
    date = models.DateField()
    button_name = models.CharField(max_length=50)
    clicks = models.IntegerField(default=0)

    class Meta:
        unique_together = ("date", "button_name")

    def __str__(self):
        return f"{self.date} {self.button_name}: {self.clicks}"


# Create your models here.
