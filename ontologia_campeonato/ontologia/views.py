from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import owlready
from owlready2 import *

# Create your views here.
def index(request):
    return redirect('/ontologia')

def index_campeonato(request):
    title = "Ontologia de Campeonato"

    read_owl_file()
    table_title = ''
    query_result = []

    if request.POST:
        print(request.POST['entidade'])

        table_title = request.POST['entidade'].capitalize()
        print(table_title)
        query_params = []
        query_params.append(request.POST['entidade'])
        query_result = make_query(query_params)

    template = loader.get_template('campeonato.html')
    context = {
        "title": title,
        "table_title": table_title,
        "result": query_result,
    }

    return HttpResponse(template.render(context, request))

def read_owl_file():
    # result = g.parse("./owl_campeonato/Campeonato-Final.owl")

    # onto_path.append("./owl_campeonato/campeonato.owl")
    get_ontology("./owl_campeonato/campeonato.owl").load()

    # print(onto.CampeonatoEsportivo)
    # print(onto.BrunoH.possuiNome)

    # default_world.set_backend(filename = "./triples.sqlite3")
    # default_world.save()


def make_query(query_params):
    graph = default_world.as_rdflib_graph()

    if len(query_params) == 1:
        string = """PREFIX camp: <http://www.campeonatobrasileirodefutebol.com/ontologies/campeonato.owl#>
                            SELECT ?{}
                            WHERE {} """.format(query_params[0], '{')+"?{} ".format(query_params[0])+"camp:atletaDe "+"?x .{}".format('}')
                            # +"{}".format(query_params[0])+" ?x .}"
        print(string)
        r = list(graph.query(string))

    # r = list(graph.query("""PREFIX ex: <http://www.campeonatobrasileirodefutebol.com/ontologies/campeonato.owl#>

    #                         SELECT ?atleta ?possuinome
    #                         WHERE {?atleta ex:atletaDe ?x ;
    #                                ex:possuiNome ?possuinome}"""))
    print(r)

    return r