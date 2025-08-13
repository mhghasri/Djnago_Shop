from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator

# Create your views here.

def articles(request):

    # ---------- articles query ---------- #

    categories = Category.objects.all()
    
    # ---------- articles query ---------- #

    # articles = Article.objects.all()
    articles = Article.objects.select_related('author','category')

    # ---------- sort ---------- #

    search = request.GET.get('q')

    if search:
        articles = articles.filter(title__icontains=search)
    
    # ---------- sort ---------- #

    sort = request.GET.get('sort')

    if sort == 'popular':
        articles = articles.order_by('-views')

    elif sort == 'newest':
        articles = articles.order_by('-created_at')

    elif sort == 'oldest':
        articles = articles.order_by('created_at')

    else:
        articles = articles.order_by('-views')

    # ---------- category ---------- #

    category_param = request.GET.get('category')

    if category_param:
        articles = articles.filter(category__slug=category_param)       # filter articles by they categories
    
    # ---------- paginator ---------- #

    paginator = Paginator(articles, 9)

    page_nmber = request.GET.get('page')

    articles = paginator.get_page(page_nmber)

    query_params = request.GET.copy()

    if 'page' in query_params:
        del query_params['page']

    query_string = query_params.urlencode()

    # ---------- total ---------- #

    count = len(list(articles))

    # ---- context ---- #

    context = {

        # articles
        'articles' : articles,

        # total
        'total' : count,

        # category
        'category' : categories,

        # pagination
        "base_url" : f"?{query_string}&" if query_string else "?",

        "clear_filter_url" : f"{request.path}?page={page_nmber}" if page_nmber else request.path,

    }

    return render(request, 'articles.html', context)

def article_details(request, **kwargs):
    context = {

    }

    return render(request, 'article_details.html', context)