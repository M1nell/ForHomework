from django.db import models
# Create your models here.
class advertisement(models.Model):
    title = models.CharField("name",max_length=120)
    descriptions = models.TextField()
    price = models.DecimalField("price", max_digits=9, decimal_places=2)
    trade = models.BooleanField("trade", help_text="If you wanna trade")
    date_now = models.DateField("Date of creation", auto_now_add= True)
    date_update = models.DateField("Update date", auto_now= True)

def __str__(self):
    return f'advertisement(id = {self.id},title = {self.title}, price = {self.price} '

class Meta:
    db_table = 'advertisements'

