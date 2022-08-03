from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import ProductSerializer

from .models import Category, Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['get'], detail=False)
    def category(self, request, pk=None):
        cats = Category.objects.all()
        return Response({c.id : c.name for c in cats})
