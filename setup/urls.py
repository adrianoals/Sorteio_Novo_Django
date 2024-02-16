from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('sorteio_novo.urls')), 
	path('', include('sorteio_novo_institucional.urls')), 
    path('', include('chacara_bom_sucesso.urls')), 
]



