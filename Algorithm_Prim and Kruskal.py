import heapq

import networkx as nx
import matplotlib.pyplot as plt
#Class representing a single Node in a graph
class Node(object):
    
    def __init__(self,height,nodeId,parentNode):
        self.height=height
        self.nodeId=nodeId
        self.parentNode=parentNode
        
#Class representing a single vertex in a graph
class Vertex(object):
    
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predecessor=None
        self.adjacenciesList=[]

#Class representing a single Edge in a graph

class Edge(object):
    
    def __init__(self,weight,source,goal):
        self.weight=weight
        self.source=source
        self.goal=goal
        
    def __cmp__(self,otherEdge):
        return self.cmp(self.weight,otherEdge.weight)
    
    def __lt__(self,other):
        return self.weight<other.weight


# Minimum Spanning Tree of a given connected, 
# undirected and weighted graph
 
class union_find(object):

    def __init__(self,vertexList):
        self.vertexList=vertexList
        self.rootNodes=[]
        self.nodeCount=0
        self.setCount=0
        self.makeSets(vertexList)
    # A utility function to find set of an node and his id 
    def find(self,node):
        currentNode=node
        while currentNode.parentNode is not None:
            currentNode=currentNode.parentNode
        root=currentNode
        currentNode=node
        while currentNode is not root:
            temp=currentNode.parentNode
            currentNode.parentNode=root
            currentNode=temp
            
        return root.nodeId
    
    def union (self,node1,node2):
        index1=self.find(node1)
        index2=self.find(node2)
        
        if index1==index2:return
        root1=self.rootNodes[index1]
        root2=self.rootNodes[index2]
        
        if root1.height<root2.height:
            root1.parentNode=root2
        elif root1.height>root2.height:
            root2.parentNode=root1
        else:
            root2.parentNode=root1
            root1.height +=1
        
        self.setCount -=1
            
            
        
        
        
    def makeSets(self,vertexList):
        for v in vertexList:
            self.makeSet(v)
            
    def makeSet(self,vertex):
        node=Node(0,len(self.rootNodes),None)
        vertex.parentNode=node
        self.rootNodes.append(node)
        self.setCount +=1
        self.nodeCount +=1
        
 # The main function to construct MST using Kruskal's 
          
class Kruskal(object):
    def constructSpanningTree(self,vertexList,edgeList):
        disjoinSet=union_find(vertexList)
        spanningTree=[]
        edgeList.sort()
        for edge in edgeList :
            u=edge.source
            v=edge.goal
            
            if disjoinSet.find(u.parentNode) is not disjoinSet.find(v.parentNode):
                spanningTree.append(edge)
                disjoinSet.union(u.parentNode,v.parentNode)
        for edge in spanningTree:
            print ("minimum Spaning Tree for Kruskal :"+edge.source.name,"-",edge.goal.name)

class Prim(object):
    def __init__(self,unvisitedList):
        self.unvisitedList= unvisitedList
        self.spanningTree=[]
        self.edgeHeap=[]
        self.mst=0
        # A utility function to print the constructed MST stored in parent[]

    def constructSpanningTree(self,vertex):
        self.unvisitedList.remove(vertex)
        
        while self.unvisitedList:
            
            for edge in vertex.adjacenciesList:
                if edge.goal in self.unvisitedList:
                    heapq.heappush(self.edgeHeap,edge)
            
            minEdge= heapq.heappop(self.edgeHeap)
            if minEdge.goal in self.unvisitedList:
                self.spanningTree.append(minEdge)
                print("minimum spanning tree for Prim: %s - %s" %(minEdge.source.name,minEdge.goal.name))
                self.mst+=minEdge.weight
                vertex=minEdge.goal
             
                self.unvisitedList.remove(vertex)
            
    def getSpanningTree(self):
        return self.spanningTree

   

node1=Vertex("1")
node2=Vertex("2")
node3=Vertex("3")
node4=Vertex("4")
node5=Vertex("5")
node6=Vertex("6")
node7=Vertex("7")

edge1=Edge(2,node1,node2)
edge2=Edge(3,node2,node5)
edge3=Edge(4,node2,node3)
edge4=Edge(3,node1,node3)
edge5=Edge(3,node1,node4)
edge6=Edge(5,node3,node4)
edge7=Edge(1,node3,node5)
edge8=Edge(7,node4,node6)
edge9=Edge(8,node5,node6)
edge10=Edge(9,node6,node7)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge4)
node1.adjacenciesList.append(edge5)
node2.adjacenciesList.append(edge2)
node2.adjacenciesList.append(edge3)
node3.adjacenciesList.append(edge6)
node3.adjacenciesList.append(edge7)
node4.adjacenciesList.append(edge8)
node5.adjacenciesList.append(edge9)
node6.adjacenciesList.append(edge10)

vertexList=[]
vertexList.append(node1)
vertexList.append(node2)
vertexList.append(node3)
vertexList.append(node4)
vertexList.append(node5)
vertexList.append(node6)
vertexList.append(node7)


A=[]
A.append(node1)
A.append(node2)
A.append(node3)
A.append(node4)
A.append(node5)
A.append(node6)
A.append(node7)

edgeList=[]
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)
edgeList.append(edge10)



prim=Prim(vertexList)
prim.constructSpanningTree(node1)
kruskal=Kruskal()
kruskal.constructSpanningTree(A,edgeList)



G=nx.Graph()
G.add_nodes_from(['1','2','3','4','5','6','7'])
G.add_edge('1','2',color='r',weight=2)
G.add_edge('1','3',color='r',weight=3)
G.add_edge('1','4',color='r',weight=3)
G.add_edge('2','3',color='r',weight=4)
G.add_edge('3','4',color='r',weight=5)
G.add_edge('2','5',color='r',weight=3)
G.add_edge('4','6',color='r',weight=7)
G.add_edge('5','6',color='r',weight=8)
G.add_edge('6','7',color='r',weight=9)
G.add_edge('3','5',color='r',weight=1)

mst=nx.minimum_spanning_edges(G,algorithm='kruskal')
arret=list(mst)

pos = nx.circular_layout(G)
#ar->arret
arr = G.edges()

i=0
l=len(arret)
for u,v in arr:
    for i in range(l):
        if ((u==arret[i][0]) and (v==arret[i][1])):
            G[u][v]['color']='b'
           
            
colors = [G[u][v]['color'] for u,v in arr]
labels = nx.get_edge_attributes(G,'weight')
plt.figure(1)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw(G, pos, arr=arr, edge_color=colors)





pr=nx.minimum_spanning_edges(G,algorithm='prim')
arret_1=list(pr)


pos_2 = nx.circular_layout(G)

arr_2 = G.edges()

iter_2=0
ll=len(arret_1)

for u,v in arr_2:
    for iter_2 in range(ll):
        if ((u==arret_1[iter_2][0]) and (v==arret_1[iter_2][1])):
            G[u][v]['color']='b'
            
color_2 = [G[u][v]['color'] for u,v in arr_2]
labelspr = nx.get_edge_attributes(G,'weight')
plt.figure(2)
nx.draw_networkx_edge_labels(G,pos_2,edge_labels=labelspr)
nx.draw(G, pos_2, arr_2=arr_2, edge_color=color_2)


plt.show()




