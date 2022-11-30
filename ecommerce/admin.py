from django.contrib import admin

# Register your models here.
from .models import Cidade
from .models import Comentarios
from .models import Tag
from .models import Video
from .models import Canal
admin.site.register(Cidade)
admin.site.register(Comentarios)
admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(Canal)

