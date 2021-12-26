from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('roadnottaken', views.roadnottaken, name='roadnottaken'),
    path('ozymandias', views.ozymandias, name='ozymandias'),
    path('if', views.if_p, name='if'),
    path('poesias', views.poesias, name='poesias'),
    path('poesias/<int:poesia_id>', views.poesia, name='poesia'),
    path('pinturas', views.pinturas, name='pinturas'),
    path('pinturas/<int:pintura_id>', views.pintura, name='pintura')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ^ A operação acima "+ static" é essencial para a exibição de imagens, sem isso o url não recebe permissoes necessárias
