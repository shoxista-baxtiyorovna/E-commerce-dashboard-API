from rest_framework import viewsets
from .serializers import CategorySerializer, CategoryDetailSerializer
from .pagination import PageNumberPagination
from .models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        return CategoryDetailSerializer
