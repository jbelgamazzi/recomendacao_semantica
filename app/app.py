"""
@import rdflib external lib
"""
import rdflib

jsonldData = open("LearningObjectsExpanded.jsonld").read()
queryData = open("findRecommendations.query").read()

graph = rdflib.Graph()
graph.parse(data=jsonldData,format='json-ld')

results = graph.query(queryData)

for result in results:
  print(result)
