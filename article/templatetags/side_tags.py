from django import template
from article.models import Category, Article



register = template.Library()

@register.simple_tag(name="category")
def all_categories():
    return Category.objects.all()

@register.simple_tag(name="popular")
def all_popular():
    return Article.objects.order_by('-hit')[:5]

