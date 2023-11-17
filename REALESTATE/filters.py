import django_filters 
from django_filters import DateFilter,CharFilter

from .models import *

class PropertyFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name = "date_of_listing", lookup_expr="gte")
    end_date = DateFilter(field_name = "date_of_listing", lookup_expr="lte")
    location = CharFilter(field_name = "location",lookup_expr="icontains")
    class Meta:
        model = Property
        fields = ["tag","list",]