from django.contrib import admin
from django.urls import include, path

from garagem.views import MarcaViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"marcas", MarcaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
