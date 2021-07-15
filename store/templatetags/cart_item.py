from django import template
# from django.template.defaultfilters import stringfilter
register = template.Library()


@register.filter(name='item_in_cart')
def item_in_cart(product,cart):
    key=cart.keys()
    for id in key:
        if int(id)==int(product.id):
            return True
    return False

@register.filter(name='items_no')
def items_no(product,cart):
    key=cart.keys()
    for id in key:
        if int(id)==int(product.id):
            return cart.get(id)
           

    
@register.filter(name='item_total')
def item_total(product,cart):
    return product.price * items_no(product, cart)

@register.filter(name='total_cart_amount')
def total_cart_amount(allproducts,cart):
    sum=0
    for s in allproducts:
        sum+=item_total(s, cart)
    return sum

@register.filter(name='total_cart_item')
def total_cart_item(allitem,cart):
    sum=0
    for bagged in allitem:
        sum+=items_no(bagged, cart)
    return sum