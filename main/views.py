from django.shortcuts import render
from products.models import Product
from articles.models import Article

def home_page(request):

    # ----- query ----- #
    products = Product.objects.all()

    articles = Article.objects.all()

    # ----- special sells ----- #

    only_discounted = products.filter(discount__gt=0)

    new_products = products.order_by('-created_at')

    popular_articles = articles.order_by('-views')
    
    context = {
        'products' : products,
        'articles' : articles,
        'only_discounted' : only_discounted,
        'new_products' : new_products,
        'popular_articles' : popular_articles,
    }
    return render(request, 'index.html', context)