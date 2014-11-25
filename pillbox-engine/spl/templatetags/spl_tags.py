from django import template

from spl.models import SetInfo, ProductData, Source, Ingredient

register = template.Library()


@register.inclusion_tag('pillbox-engine/tags/widgets.html')
def spl_widgets():
    products_count = SetInfo.objects.all().count()
    pills_count = ProductData.objects.all().count()
    source_count = Source.objects.all().count()
    ingredient_count = Ingredient.objects.all().count()

    boxes = [
        {
            'icon': 'fa-stethoscope',
            'name': 'SPL Products',
            'count': products_count,
            'text': 'Sync Data',
            'link': '#',
            'color': 'primary'
        },
        {
            'icon': 'fa-medkit',
            'name': 'OSDF Pills',
            'count': pills_count,
            'text': 'Sync Data',
            'link': '#',
            'color': 'green'
        },
        {
            'icon': 'fa-recycle',
            'name': 'Ingredients',
            'count': ingredient_count,
            'text': 'View Details',
            'link': '#',
            'color': 'yellow'
        },
        {
            'icon': 'fa-download',
            'name': 'Sources',
            'count': source_count,
            'text': 'View Details',
            'link': '#',
            'color': 'red'
        }]

    return {'boxes': boxes}