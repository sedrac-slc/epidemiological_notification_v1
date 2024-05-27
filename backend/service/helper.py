from django.core.paginator import Paginator

def paginator(request, data):
    page_data = Paginator(data, 2)
    page_num = request.GET.get('page')
    return page_data.get_page(page_num)