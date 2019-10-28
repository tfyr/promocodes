import graphene
from datetime import datetime

from telegram.telegram import send_mess

from promocodes.models import Promoused, Promo

CART_ID = 'CART-ID'

class UsedPromoType(graphene.ObjectType):
    id = graphene.ID()
    code = graphene.String()
    discountpercent = graphene.Decimal()
    discountsumma = graphene.Decimal()
    cancel = graphene.Boolean()


class Query(object):
    pass


class ApplyPromo(graphene.Mutation):
    ok = graphene.Boolean()
    #used = graphene.List(UsedPromoType)

    class Arguments:
        promo = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, **args):
        ok = False
        cart_id=info.context.session.get(CART_ID)
        if args.get('promo') == 'clear':
            Promoused.objects.filter(cart_id=cart_id).delete()
        elif args.get('promo') == 'telegram':
            send_mess(448010439, "Тест телеграмма")
        else:
            try:
                code=Promo.objects.get(code=args.get('promo'), start__lte=datetime.now(), finish__gte=datetime.now())
                try:
                    Promoused.objects.get(cart_id=cart_id, code=code, )
                except Promoused.DoesNotExist:
                    promo = Promoused(cart_id=cart_id, code = code)
                    promo.save()
                else: #ItemAlreadyExists
                    pass
                ok = True
            except Promo.DoesNotExist:
                ok = False
        #realdiscount, arr = get_promos(cart)
        return cls(
            ok=ok,
        #    used=arr
        )

class Mutation():
    applypromo = ApplyPromo.Field()
