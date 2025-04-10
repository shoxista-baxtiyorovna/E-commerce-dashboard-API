from rest_framework import serializers
from .models import Category


class ProductCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=10)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'parent',
            'image',
            'created_at',
        ]


class CategoryDetailSerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        fields = super().fields = ['parent_name', 'parent_info']

        def get_parent_name(self, instance):
            return instance.parent.name

        def get


# class CategoryDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(read_only=True)
#     description = serializers.CharField(read_only=True)
#     parent = serializers.IntegerField(read_only=True)
#     parent_name = serializers.SerializerMethodField()
#     image = serializers.ImageField(read_only=True)
#     products_info = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#
#     def get_parent_name(self, obj):
#         return obj.parent.name
#
#
#     def get