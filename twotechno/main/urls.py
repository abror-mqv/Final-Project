from django.urls import path
from .views import index #laptops, tablets, cams, buy
urlpatterns = [
    path("", index, name="index"),
    # path('laptops', laptops, name='laptops'),
    # path('tablets', tablets, name='tablets'),
    # path('cams', cams, name='cam'),
    # path('how-to-buy', buy, name='buy'),
]