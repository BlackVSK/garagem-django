from rest_framework.viewsets import ModelViewSet
from garagem.serializers import MarcaSerializer, CategoriaSerializer, AcessorioSerializer, CorSerializer, VeiculoSerializer, VeiculoDetailsSerializer, VeiculoListSerializer
from garagem.models import Marca, Categoria, Acessorio, Cor, Veiculo

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailsSerializer
        return VeiculoSerializer