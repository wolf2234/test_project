from .models import *
import random
import string

def getting_basket_info(request):
    session_key = request.session.get('session_key', False)
    if not session_key:
        request.session['session_key'] = ''.join(random.choices((string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters), k=8))
        request.session.modified = True

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    product_total_nmb = products_in_basket.count()
    return locals()




