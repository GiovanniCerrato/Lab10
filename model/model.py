import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMapCountry = {}
        for c in DAO.getAllCountry():
            self._idMapCountry[c.CCode] = c

    def buildGraph(self,x):
        self._grafo.clear()
        nodi = DAO.getAllNodes(x)
        for n in nodi:
            self._grafo.add_node(self._idMapCountry[n[0]])

        edges = DAO.getAllEdges(x)
        for e in edges:
            c1=e[0]
            c2=e[1]
            self._grafo.add_edge(self._idMapCountry[c1],self._idMapCountry[c2])

    def getRaggiungibili(self,source):
        raggiungibili = nx.node_connected_component(self._grafo, source)
        raggiungibili = list(raggiungibili)
        raggiungibili.sort(key=lambda r:r.StateNme)
        return raggiungibili[1:],len(raggiungibili)-1

    def getAllNodes(self):
        return self._grafo.nodes()
    def getAllEdges(self):
        return self._grafo.edges()
    def getNumConfinantiStato(self,country):
        return len(list(self._grafo.neighbors(country)))
    def getNumCompConnesse(self):
        return nx.number_connected_components(self._grafo)


