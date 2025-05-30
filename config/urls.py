from django.contrib import admin
from django.urls import include, path

from garagem.views import MarcaViewSet, CorViewSet, AcessorioViewSet, CategoriaViewSet, VeiculoViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"veiculos", VeiculoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
