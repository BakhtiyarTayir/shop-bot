from rest_framework import serializers


from .models import Product
from .models import Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Product
        fields = ("title", "category")


class ProductsByCategorySerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    id = serializers.CharField()

    class Meta:
        model = Product
        fields = ("id", "title")
