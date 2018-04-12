import networkx as nx
import pylab as P
import matplotlib.pyplot as plt
def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
  
  
    if src == dest:
        # on créé the shortest path et on l'affiche
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[dest])) 
    else :     
      
        if not visited: 
            distances[src]=0
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src

        visited.append(src)

        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)
        


if __name__ == "__main__":
    graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
    #dijkstra(graph,'c','b')
    
    
    print("-------------------------------")
    G=nx.Graph()
    G.add_nodes_from(['a','b','c','d','s','t'])
    G.add_weighted_edges_from([('s','b',1),('s','a',2),('a','s',3),('a','b',4),('a','c',8),('b','s',4),('b','a',2),('b','d',2),
                               ('c','a',2),('c','d',7),('c','t',4),
                      ('d','b',1),('d','c',11),('d','t',5),('t','c',3),('t','d',5)])
    
    l= nx.dijkstra_path(G,'b','t')
  

    for p in G.edges():
        G[p[0]][p[1]]['color'] = 'black'
    for i in range(len(l)-1):
        G[l[i]][l[i+1]]['color'] = 'blue'
    # Store in a list to use for drawing
    edge_color_list = [ G[p[0]][p[1]]['color'] for p in G.edges() ]
    nx.draw(G,edge_color = edge_color_list, with_labels = True)

