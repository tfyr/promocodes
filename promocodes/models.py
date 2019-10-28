from django.db import models


class Promo(models.Model): # Промокоды
    code = models.CharField('Промо-код', max_length=50, unique=True)
    start = models.DateField(verbose_name="Старт", null=True, default=None, blank=True)
    finish = models.DateField(verbose_name="Окончание", null=True, default=None, blank=True)
    #kitem = models.ForeignKey(KItem, verbose_name='Подарок', null=False, blank=False, default=None)
    discountpercent = models.DecimalField(verbose_name="Скидка в процентах", null=True, default=None, blank=True, max_digits=11, decimal_places=2)
    discountsumma = models.DecimalField(verbose_name="Скидка суммой", null=True, default=None, blank=True, max_digits=11, decimal_places=2)
    def __str__ (self):
        return self.code
    class Meta:
        ordering = ['code']
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"


class Promoused(models.Model):
    cart_id = models.IntegerField(null=True) #.ForeignKey(Cart, verbose_name='cart', on_delete=models.CASCADE)
    code = models.ForeignKey(Promo, verbose_name='code', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Промокод в корзине"
        verbose_name_plural = "Промокоды в корзине"
        unique_together = (
            'cart_id',
            'code',
        )
    def __str__(self):
        return self.code
