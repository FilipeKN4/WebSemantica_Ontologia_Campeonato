from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return redirect('/ontologia')

def index_campeonato(request):
    title = "Ontologia de Campeonato"

    template = loader.get_template('campeonato.html')
    context = {"title": title}

    return HttpResponse(template.render(context, request))