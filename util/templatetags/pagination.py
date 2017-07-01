#template tag para gerar a paginação nas paginas que precisa
from django.template import Library

register = Library()


@register.inclusion_tag('pagination.html')#util/templates
def pagination(request,paginator,page_obj):
    context = {}
    context['paginator'] = paginator
    context['request'] = request
    context['page_obj'] = page_obj
    return context
