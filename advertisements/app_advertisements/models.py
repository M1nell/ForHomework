from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class advertisement(models.Model):
    title = models.CharField("name",max_length=120)
    descriptions = models.TextField("description")
    price = models.DecimalField("price", max_digits=9, decimal_places=2)
    trade = models.BooleanField("trade", help_text="If you wanna trade")
    date_now = models.DateTimeField("Date of creation", auto_now_add= True)
    date_update = models.DateTimeField("Update date", auto_now= True)
    image = models.ImageField("Image path", upload_to='advertisements/')
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True)

    def __str__(self):
        return f'advertisement(id = {self.id},title = {self.title}, price = {self.price} '

    class Meta:
        db_table = 'advertisement'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


    @admin.display(description="Time of creation")
    def created_date(self):
        from django.utils import timezone
        if self.date_now.date() ==timezone.now().date():
            created_time = self.date_now.time().strftime("%H:%M:%S")
            return format_html(
                '<span style = "color:green; font-weight: bold;"> Today at {}</span>',created_time
            )
        return self.date_now.strftime("%d.%m.%y at %H:%M:%S")

    @admin.display(description="Image")
    def img(self):
        if self.image:
            return format_html(
                '<img scr = "/media/{}"  width = "75" height = "75"/>',self.image
            )
        else:
            return format_html(
                '<img scr = "/static/img/adv.png"  width = "75" height = "75"/>',self.image
            )

