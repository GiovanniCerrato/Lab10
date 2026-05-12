import networkx as nx

# Grafo NON orientato
grafo = nx.Graph()

# Aggiungo i nodi
grafo.add_nodes_from(['USA', 'CAN', 'MEX'])

# Aggiungo archi "duplicati" con nodi invertiti
grafo.add_edge('USA', 'CAN')
grafo.add_edge('CAN', 'USA')  # Questo NON crea un nuovo arco!

print(f"Numero di archi: {grafo.number_of_edges()}")  # Output: 1
print(f"Archi: {list(grafo.edges())}")  # Output: [('USA', 'CAN')]