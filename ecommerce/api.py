from rest_framework import routers, serializers, viewsets, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.viewsets import ViewSet

from ecommerce.models import Cidade
from ecommerce.models import Comentarios
from ecommerce.models import Tag
from ecommerce.models import Video
from ecommerce.models import Canal

#### Cidades ########################################
class CidadeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cidade
    fields = ['id', 'nome']

class CidadeViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Cidade.objects.all().order_by('nome')
  serializer_class = CidadeSerializer 
######################################################

  
#### Comentarios ########################################
class ComentariosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comentarios
    fields = ['texto', 'nome']

class ComentariosViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Comentarios.objects.all().order_by('nome')
  serializer_class = ComentariosSerializer 
######################################################

#### Tag ########################################
class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ['nome']

class TagViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Tag.objects.all().order_by('nome')
  serializer_class = TagSerializer 
######################################################

#### Video ########################################
class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = ['titulo', 'descricao', 'data' , 'youtubeid', 'thumb']

class VideoViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Video.objects.all().order_by('titulo')
  serializer_class = VideoSerializer 
  def get_queryset(self):

    """
    Filtra video por titulo 
    """
    queryset = Video.objects.all().order_by('titulo')
    query = {}

    titulo = self.request.query_params.get('titulo', None)
    if titulo is not None:
      query['titulo'] = titulo

    """
    Filtra video por canal
    """
    queryset = Video.objects.all().order_by('canal')
    query = {}

    canal = self.request.query_params.get('canal', None)
    if canal is not None:
      query['canal'] = canal

    """
    Filtra video por tag
    """
    queryset = Video.objects.all().order_by('tag')
    query = {}

    tag = self.request.query_params.get('tag', None)
    if tag is not None:
      query['tag'] = tag

    print(query)
    queryset = queryset.filter(**query)    
    return queryset
######################################################

#### Canal ########################################
class CanalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Canal
    fields = ['titulo','descricao', ]

class CanalViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Canal.objects.all().order_by('nome')
  serializer_class = CanalSerializer ######################################################


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cidades', CidadeViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'tag', TagViewSet)
router.register(r'video', VideoViewSet)