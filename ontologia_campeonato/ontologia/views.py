from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from owlready2 import *

# Create your views here.
def index(request):
    return redirect('/ontologia')

def index_campeonato(request):
    title = "Ontologia de Campeonato"

    read_owl_file()
    query = make_query()

    template = loader.get_template('campeonato.html')
    context = {
        "title": title,
        "resultado": query,
    }

    return HttpResponse(template.render(context, request))

def read_owl_file():
    # result = g.parse("./owl_campeonato/Campeonato-Final.owl")

    # onto_path.append("./owl_campeonato/campeonato.owl")
    onto = get_ontology("./owl_campeonato/camp.owl").load()
    # onto = onto_path[0].load()
    print(onto.CampeonatoEsportivo)
    print(onto.BrunoH.possuiNome)

    # default_world.set_backend(filename = "./triples.sqlite3")
    # default_world.save()
    
    # import campeonato
    # # onto = onto_path.load()
    # print(campeonato.Campeonato)

def make_query():
    graph = default_world.as_rdflib_graph()
    print(graph)
    r = list(graph.query("""PREFIX ex: <http://www.campeonatobrasileirodefutebol.com/ontologies/campeonato.owl#>

                            SELECT ?atleta ?possuinome
                            WHERE {?atleta ex:atletaDe ?x ;
                                   ex:possuiNome ?possuinome}"""))
    print(r[0])

    return r