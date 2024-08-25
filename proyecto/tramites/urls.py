from django.urls import path
from . import views

app_name = "tramites"

urlpatterns = [
    path("", views.index, name="index"),
    path("tipodetramite/list", views.tipodetramite_list, name="tipodetramite_list"),
    path("tramite/list", views.tramite_list, name="tramite_list"),
]
