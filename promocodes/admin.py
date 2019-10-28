from django.contrib import admin

# Register your models here.
from promocodes.models import Promo

class PromoAdmin(admin.ModelAdmin):

    list_display = (
        'code',
        'start',
        'finish',
        'discountpercent',
        'discountsumma',
    )

admin.site.register(Promo, PromoAdmin)
