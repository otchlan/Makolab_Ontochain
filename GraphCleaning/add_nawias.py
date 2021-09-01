from rdflib import Graph, URIRef
# from owlready2 import IRIS
from rdflib import Namespace

g1 = Graph()
g2 = Graph()

g = Graph()
gg = Graph()

g1 = g1.parse("geo.ttl")
g2 = g2.parse("geo2.ttl")

x = "<class 'rdflib.term.Literal'>"


for q, w, e in g1.triples((None, None, None)):
    i = str(type(e))
    if i == x:
        conc = Namespace("http://example.org/country/")
        r = str(e)
        r = r.replace(" ", "_")
        g.add((q, w, conc.term(r)))
        # urf = URIRef("http://example.org/people/")
        # print(con)
    else:
        g.add((q, w, e))

for q, w, e in g2.triples((None, None, None)):
    i = str(type(e))
    if i == x:
        # print(str(e))
        conc = Namespace("http://example.org/country/")
        r = str(e)
        r = r.replace(" ", "_")

        gg.add((q, w, conc.term(r)))
        # urf = URIRef("http://example.org/people/")
        # print(con)
    else:
        gg.add((q, w, e))
        i = 0


g.serialize(destination='output1.ttl')
gg.serialize(destination='output2.ttl')




# g1 = open('geo.ttl', 'r+')
# g1 = str(g1)
# g2 = open('geo2.ttl', 'r+')
# gg2 = str(g2)

# g = g1.read()
# print(g)

# a = 0
# el = '\"'
# x = 0
#
# for aline in g1:
#     # for element in range(len(aline)):
#     values = aline.split()
#     length = len(values)                # values = aline.split()
#
#     for i in range(length):
#     #     value = values.split()
#         value = values[i]
#         length = len(value)
#         for i in range(length):
#             # print(value[i])
#             if value[i] == el and a == 0:
#                 x += 1
#                 # print(type(value[i]))
#                 # print("1 --", value[i])
#                 # v = value[i].replace('"', "<")
#                 # print("2 --", value[i])
#                 a = 1
#             #     print(vaule)
#             elif value[i] == el and a == 1:
#                 str1 = value[i]
#                 # print("3 --", value[i])
#                 # v = value[i].replace('"', ">")
#                 # print("4 --", value[i])
#                 # print("5 --", v)
#                 a = 0


    # print(values)
# print(x)
        # if value == el and i == 1:
        #     value = '<'
        #     i = 1
        #     print(vaule)
        # elif value == el and i == 1:
        #     value = ">"
        #     i = a

# g1.write(str(gg1))
# g2.write(str(gg2))
# g1.close()
# g2.close()

# print(g1)
