
from django.urls import path
from products import views
from django.urls import path
from .views import login_view
from products.views import ProductListCreateView, ProductRetrieveUpdateDeleteView
from .api_views import ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('login/', login_view, name='login'),
]

