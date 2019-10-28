from django.shortcuts import render

# Create your views here.
'''
def reg_promo(self, code):
    try:
        promo = models.Promoused.objects.get(
            cart=self.cart,
            code=code,
        )
    except models.Promoused.DoesNotExist:
        promo = models.Promoused()
        promo.cart = self.cart
        promo.code = code
        promo.save()
    else:  # ItemAlreadyExists
        pass
'''