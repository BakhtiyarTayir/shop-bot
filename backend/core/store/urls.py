from django.urls import path, include

from . import views
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'product', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('product_list/<int:pk>', views.ProductListByCatView.as_view()),
    # path('product/<int:pk>', views.SingleProductViewSet.as_view()),
]