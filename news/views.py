from django.shortcuts import render,redirect, get_object_or_404
from django.core.mail import send_mail
from .models import NewsItem
from .forms import NewsItemForm

def index(request):
    context={}
    return render(request, "news/index.html", context)

def news_view(request):
    news_items = NewsItem.objects.all()

    if request.method == 'POST':
        form = NewsItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsItemForm()

    return render(request, 'news/news_detail.html', {'news_items': news_items, 'form': form})
