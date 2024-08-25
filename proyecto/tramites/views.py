from django.shortcuts import render
from .models import TipoDeTramite, Tramite


def index(request):
    return render(request, "tramites/index.html")


def tipodetramite_list(request):
    tipostramites = TipoDeTramite.objects.all()
    contexto = {"tipostramites": tipostramites}
    return render(request, "tramites/tipodetramite_list.html", contexto)


def tramite_list(request):
    tramites = Tramite.objects.all()
    contexto = {"tramites": tramites}
    return render(request, "tramites/tramite_list.html", contexto)
