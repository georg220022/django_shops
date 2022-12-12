from .views import ShopViewSet, ProductList
from django.urls import path

urlpatterns = [
    path("all", ProductList.as_view()),
    path("<int:id>", ShopViewSet.as_view({"get": "get_product"})),
    path("add", ShopViewSet.as_view({"post": "add_product"})),
]
