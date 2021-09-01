import fastapi
import uvicorn
from rdflib import URIRef, Graph, Literal
from rdflib.namespace import FOAF, RDF
import json

g = Graph()
g.parse("geo.ttl")

def get_json(n=0):

    lista = []
    for sub, pre, obj in g.triples((None, None, None)):
    # for sub, pre, obj in g:
        triple = (sub, pre, obj)
        lista.append(triple)

    i = 0
    dictionary = {}

    for triple in lista:
        dictionary[str(i)] = triple
        i += 1

    # data = json.dumps(dictionary, indent=2)
    # return data
    return dictionary[str(n)]


# def getTriple(n=0):
#     dictionary = dict(get_json())
#     return type(dictionary)
    # return dictionary.keys()
    # return dictionary.value(n)

app = fastapi.FastAPI()

# @app.route('/index/<int:n>')
@app.get('/index/{n}/')
async def index(n):
    return get_json(int(n))

@app.get('/number/')
async def tripletsNumber():
    return len(g)

if __name__ == '__main__':
        uvicorn.run(app, host="127.0.0.1", port=80, debug=True)
        