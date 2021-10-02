from django.shortcuts import render
from .models import Laptop, Camera, Tablet
# Create your views here.


# def index(request):
#     return render(request, 'main/index.html')

def index(request):
    return render(request, 'main/index.html')

# class DView(DetailView):
#     model = Product
#     template_name = 'main/dview.html'
#     context_object_name = 'laptop'

# def catalog(request):
#     products = Product.objects.order_by('-price')
#     return render(request, 'main/catalog.html', {'products': products})

# def aboutus(request):
#     return render(request, 'main/about-us.html')