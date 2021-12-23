from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('roadnottaken', views.roadnottaken, name='roadnottaken'),
    path('ozymandias', views.ozymandias, name='ozymandias'),
    path('if', views.if_p, name='if'),
    path('poesias', views.poesias, name='poesias')
]