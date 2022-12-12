from django_filters import rest_framework as filters
from product.models import Product


class ProductFilter(filters.FilterSet):
    status = filters.CharFilter(field_name="status")
    vendor_code = filters.NumberFilter(field_name="vendor_code")
    name = filters.CharFilter(field_name="name")

    class Meta:
        model = Product
        fields = ["status", "name", "vendor_code"]
