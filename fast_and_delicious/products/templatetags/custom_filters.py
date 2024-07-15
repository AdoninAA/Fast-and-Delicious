from django import template

register = template.Library()

@register.filter
def category(product, previous_category):
    if product.category.title != previous_category:
        previous_category = product.category.title
        return product.category.title
    return ''