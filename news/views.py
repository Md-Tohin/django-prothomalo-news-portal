from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import News

# Create your views here.

def news(request, category_slug=None):

    categories = None
    news = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        news = News.objects.all().filter(category=categories, is_publish=True)
        latest_5_news = News.objects.filter(category=categories,is_top=True,is_publish=True).order_by('-created_at')[:5]
        news_count = news.count()
    else:
        news = News.objects.all().filter(is_publish=True)
        latest_5_news = News.objects.filter(is_top=True,is_publish=True).order_by('-created_at')[:5]
        news_count = news.count()

    context = {
        'news': news,
        'category_name': categories,
        'latest_5_news': latest_5_news,
        'news_count': news_count,
    }

    return render(request, 'news/news.html', context)


def news_detail(request, category_slug, news_slug):    
    try: 
        
        single_news = News.objects.get(category__slug=category_slug, slug=news_slug)
        # latest_8_news = News.objects.filter(category=categories,is_top=True,is_publish=True).order_by('-created_at')[:12]
    except Exception as e:
        raise e
        # return render(request, 'store/news_not_found.html', status=404)
    
    context = {
        'single_news': single_news,
    }

    return render(request, 'news/news_detail.html', context)
