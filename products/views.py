from django.shortcuts import render, get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator

# ---------------------- products ---------------------- #

def products(request):

    # ---------- query ---------- #
    products = Product.objects.all()

    # ---------- price range ---------- #

    min_price_range = request.GET.get('min_price_range')

    max_price_range = request.GET.get('max_price_range')

    if min_price_range and max_price_range:
        products = products.filter(
            Q(final_price__gte = int(min_price_range)) & Q(final_price__lte = int(max_price_range))
        )

    # ---------- search ---------- #

    search = request.GET.get('q')

    if search:
        products = products.filter(title__icontains=search)

    # ---------- only_available ---------- #
    
    only_available = request.GET.get('only_available')

    if only_available:
        products = products.filter(is_available=True)

    # ---------- only_discounted ---------- #
    
    only_discounted = request.GET.get('only_discounted')

    if only_discounted:
        products = products.filter(discount__gt = 0)

    # ---------- sort ---------- #
    
    sort = request.GET.get('sort')

    if sort == 'newest':
        products = products.order_by('-created_at')     # old ----- new         -->     reverse=True

    elif sort == 'oldest':
        products = products.order_by('created_at')

    elif sort == 'cheap':
        products = products.order_by('final_price')     # cheap --- expensive   -->     reverse=True     

    elif sort == 'expensive':
        products = products.order_by('-final_price')

    else:
        products = products.order_by('-created_at')

    # ---------- paginator ---------- #

    paginator = Paginator(products, 9)

    page_nmber = request.GET.get('page')

    products = paginator.get_page(page_nmber)

    query_params = request.GET.copy()

    if 'page' in query_params:
        del query_params['page']

    query_string = query_params.urlencode()
    
    # ---------- total ---------- #

    count = len(list(products))

    # ---------- context ---------- #

    context = {
        # product query
        "products" : products,

        # count product
        "total" : count,

        # pagination
        "base_url" : f"?{query_string}&" if query_string else "?",

        # remove all filter
        "clear_filter_url" : f"{request.path}?page={page_nmber}" if page_nmber else request.path

    }

    return render(request, 'products.html', context)

# ---------------------- product details ---------------------- #

def product_detail(request, **kwargs):

    # for all products

    products = Product.objects.all()

    # for selected product

    product = get_object_or_404(Product.objects.prefetch_related("attribute", "gallery"), pk=kwargs["pk"])
    
    # filter special sells product

    special_sells = products.filter(special_sells=True).exclude(pk=product.id)      # except the selected product

    # filter discounted product

    discounted_product = products.filter(discount__gt = 0).exclude(pk=product.id)   # except the selected product

    context = {

        # products
        'products' : products,
        'product' : product,
        'attributes' : product.attribute.all(),
        'images' : product.gallery.all(),
        'colors' : product.colors.all(),
        'special_sells' : special_sells,
        'discounted_product' : discounted_product,
    }

    return render(request, 'product_detail.html', context)