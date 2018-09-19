from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include

from bookphone import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    path('personal-secretaria/', include([
        path('<int:id>', views.personal_secretaria, name='personal-secretaria'),
        path('nuevo', views.nuevo_personal_secre, name='nuevo_personal_secre'),
        path('<int:id>/edit/', views.edit_personal_secretaria, name='editar_personal_secre'),
        path('<int:id>/delete/', views.delete_personal_secretaria, name='delete_personal_secre'),
    ])),

    path('personal-unidad/', include([
        path('<int:id>', views.personal_unidad, name='personal-unidad'),
        path('nuevo', views.nuevo_personal_unidad, name='nuevo_personal_uni'),
    ])),

    path('secretarias/', include([
        path('<int:id>', views.list, name='list'),
        path('nuevo', views.nueva_secretaria, name='nueva_secretaria'),
        path('<int:id>/edit/', views.edit_secretaria, name='editar_secretaria'),
        path('<int:id>/delete/', views.delete_secretaria, name='delete_secretaria'),
    ])),
    path('unidades/', include([
        path('<int:id>', views.unidad, name='unidad'),
        path('nueva_unidad', views.nueva_unidad, name='nueva_unidad'),
        path('<int:id>/edit/', views.edit_unidad, name='editar_unidad'),
        path('<int:id>/delete/', views.delete_unidad, name='delete_unidad'),
    ])),
]

