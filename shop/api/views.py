from rest_framework import status, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from product.models import Product
from .serializers import ProductSerializer
from .filter import ProductFilter


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination


class ShopViewSet(viewsets.ViewSet):
    def get_permissions(self):
        return (permissions.AllowAny(),)

    def get_product(self, request, id):
        if isinstance(id, int):
            obj = get_object_or_404(Product, id=id)
            serializer = ProductSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return {"error": "id должен быть int"}

    def add_product(self, request):
        context = {"image": request.FILES.get("image", False)}
        serializer = ProductSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
