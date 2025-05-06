from django.shortcuts import render
from news.models import News

def home(request):
    is_latest_top_2_news = News.objects.filter(is_top=True, is_publish=True).order_by('-created_at')[:2]
    lagest_news = News.objects.all().filter(is_publish=True)
    is_image_4_news = News.objects.filter(is_image=True, is_publish=True).order_by('-created_at')[:4]
    context = {
        'latest_news': lagest_news,
        'is_image_4_news': is_image_4_news,
        'is_latest_top_2_news': is_latest_top_2_news,
    }

    return render(request, 'home.html', context)