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

    get_ontology("./owl_campeonato/campeonato.owl").load()
    table_title = ''
    query_result = []

    if request.POST:
        entity =  request.POST['entidade']
        object_property = request.POST['propriedade_objeto']
        datatype_property = request.POST['propriedade_dado']

        table_title = request.POST['entidade']
        query_params = []
        if entity is not '':
            query_params.append(entity)
        if object_property is not '':
            query_params.append(object_property)
        if datatype_property is not '':
            query_params.append(datatype_property)
        query_result = make_query(query_params)

    template = loader.get_template('campeonato.html')
    context = {
        "title": title,
        "table_title": table_title,
        "result": query_result,
    }

    return HttpResponse(template.render(context, request))

def make_query(query_params):
    graph = default_world.as_rdflib_graph()
    result = []
    if len(query_params) < 2:
        result = []
    elif len(query_params) == 2:
        string = """PREFIX camp: <http://www.campeonatobrasileirodefutebol.com/ontologies/campeonato.owl#>
                            SELECT ?{}
                            WHERE {} """.format(query_params[0], '{')+"?{} ".format(query_params[0])+"camp:{} ".format(query_params[1])+"?x .{}".format('}')
                            # +"{}".format(query_params[0])+" ?x .}"
        result = list(graph.query(string))
    elif len(query_params) == 3:
        string = """PREFIX camp: <http://www.campeonatobrasileirodefutebol.com/ontologies/campeonato.owl#>
                            SELECT ?{} ?{}
                            WHERE {} """.format(query_params[0], query_params[2], '{')+"?{} ".format(query_params[0])+"camp:{} ".format(query_params[1])+"?x ;"+"""
                            camp:{} """.format(query_params[2])+"?{}{}".format(query_params[2], '}')
        result = list(graph.query(string))   

    return result