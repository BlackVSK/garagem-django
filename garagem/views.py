from rest_framework.viewsets import ModelViewSet
from garagem.serializers import MarcaSerializer
from garagem.models import Marca

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer