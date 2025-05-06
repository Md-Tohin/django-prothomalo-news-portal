from .models import Category

def menu_links(request):
    links = Category.objects.all().filter(is_top=True)
    return dict(links=links)