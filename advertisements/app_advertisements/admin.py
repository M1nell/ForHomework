from django.contrib import admin
from .models import advertisement
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title','descriptions','price','trade','date_now','date_update','created_date','user','image','img']
    list_filter = ['date_now','descriptions','trade']
    fieldsets = (
        ("First block",{
            "fields":('title','descriptions','image','user')}),
        ("Second block",{
            "fields":('price','trade')}),
    )
    actions = ['make_true','make_false']
    @admin.action(description="update (trade = True)")
    def make_true(self,request,queryset):
        queryset.update(trade= True)
        pass

    @admin.action(description="update (trade = False)")
    def make_false(self,request,queryset):
        queryset.update(trade= False)
        pass





admin.site.register(advertisement,AdvertisementAdmin)

# Register your models here.
