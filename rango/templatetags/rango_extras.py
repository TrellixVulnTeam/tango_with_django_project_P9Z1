from django import template
from rango.models import Category 

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list(cat=None):
    # key ��ʾ���ݵ� cats.html �ı����� 
    # ͨ��Ӧ��ģ���е� {% get_category_list category %} ����
    return {"cats": Category.objects.all(), 'act_cat': cat}