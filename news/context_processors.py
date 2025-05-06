from .models import News

def latest_4_news(request, category_slug=None):
    categories = None
    news = None
    if category_slug != None:
        latest_4_news = News.objects.filter(category=categories, is_publish=True).order_by('-created_at')[:4]
    else:
        latest_4_news = News.objects.filter(is_publish=True).order_by('-created_at')[:4]
    return dict(latest_4_news=latest_4_news)

def is_read_4_news(request, category_slug=None):
    categories = None
    news = None
    if category_slug != None:
        is_read_4_news = News.objects.filter(category=categories, is_read=True, is_publish=True).order_by('-created_at')[:4]
    else:
        is_read_4_news = News.objects.filter(is_read=True, is_publish=True).order_by('-created_at')[:4]
    return dict(is_read_4_news=is_read_4_news)

def is_discussed_4_news(request, category_slug=None):
    categories = None
    news = None
    if category_slug != None:
        is_discussed_4_news = News.objects.filter(category=categories, is_discussed=True, is_publish=True).order_by('-created_at')[:4]
    else:
        is_discussed_4_news = News.objects.filter(is_discussed=True, is_publish=True).order_by('-created_at')[:4]
    return dict(is_discussed_4_news=is_discussed_4_news)

def is_selected_4_news(request, category_slug=None):
    categories = None
    news = None
    if category_slug != None:
        is_selected_4_news = News.objects.filter(category=categories, is_selected=True, is_publish=True).order_by('-created_at')[:4]
    else:
        is_selected_4_news = News.objects.filter(is_selected=True, is_publish=True).order_by('-created_at')[:4]
    return dict(is_selected_4_news=is_selected_4_news)