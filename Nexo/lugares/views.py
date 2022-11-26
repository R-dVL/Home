from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
import json
from django.core.serializers import serialize


from .models import Restaurante
# Create your views here.
@login_required
def restaurantes(request):
    lista_restaurantes = Restaurante.objects.order_by('-puntuacion')[:30]
    context = {'lista_restaurantes': lista_restaurantes}
    return render(request, 'lugares/restaurantes.html', context)


class Mapa(TemplateView):
    template_name = "mapa.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["restaurantes"] = json.loads(serialize("geojson", Restaurante.objects.all()))
        return context
