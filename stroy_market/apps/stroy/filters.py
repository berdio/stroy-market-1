from django_filters import rest_framework as filters
from apps.stroy.models import Category, SubCategory, Product, ProductImage, Size, Color
    

class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(field_name='category__category__slug')
    subcategory = filters.CharFilter(field_name='subcategory__slug')
    popular = filters.BooleanFilter(method='filter_popular')
    # rating = filters.BooleanFilter(method='rating', field_name='likes')
    cheaper = filters.BooleanFilter(method='filter_cheaper')
    expensive = filters.BooleanFilter(method='filter_expensive')
    price_range = filters.RangeFilter(field_name='price')
    in_discount = filters.BooleanFilter(field_name='in_discount')

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'popular', 'price_range', 'cheaper', 'expensive', 'in_discount']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['category'].label = 'Kategoriya'
        self.filters['subcategory'].label = 'Sub kategoriya'
        self.filters['popular'].label = 'Mashhur'
        # self.filters['rating'].label = 'Rating'
        self.filters['price_range'].label = 'Narx oraligi'
        self.filters['cheaper'].label = 'Arzonlari oldin'
        self.filters['expensive'].label = 'Qimmatlari oldin'
    
    def filter_popular(self, queryset, name, value):
        if value:
            return queryset.order_by('-views')
        return queryset

    def filter_cheaper(self, queryset, name, value):
        if value:
            return queryset.order_by('price')
        return queryset

    def filter_expensive(self, queryset, name, value):
        if value:
            return queryset.order_by('-price')
        return queryset
    
    # def latest(self, queryset, name, value):
    #     if value:
    #         return queryset.order_by('-created_at')
    #     return queryset
