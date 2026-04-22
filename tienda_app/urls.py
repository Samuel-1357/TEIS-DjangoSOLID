from django.urls import path
from .api.views import CompraAPIView, ProductosAPIView
from .views import CompraView, public_home

urlpatterns = [
    path('public', public_home, name='public_home_no_slash'),
    path('public/', public_home, name='public_home'),
    # Usamos .as_view() para habilitar la CBV
    path('compra/<int:libro_id>/', CompraView.as_view(), name='finalizar_compra'),
    path('api/v1/productos/', ProductosAPIView.as_view(), name='api_productos'),
    path('api/v1/comprar/', CompraAPIView.as_view(), name='api_comprar'),
]