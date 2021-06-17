from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('chat/',views.ChatterBotAppView.as_view(), name='chatwithpete'),
    path('chat/api/chatterbot/', views.ChatterBotApiView.as_view(), name='pete')
]