from queue import *
class Node:
    def __init__(self, vex, Weight):
        self.vex = vex
        self.path = []
        self.Weight = Weight
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def shortest_path(vertex):
   Visted = set()
   q = QueueArray(100)
   Target = None
   v= None
   for v in g:
       if v.getId() == vertex:
           Target = v.getId()
           break
   if Target == None:
       raise ValueError("Not In Graph")
   Vertics_lis ={}
   q.enqueue(v)
   Visted.add(v)
   Vertics_lis[v.getId()] = [Target, 0]
   while q.is_empty() == False:
        v2 = q.dequeue()
        for w in v2.getConnections():
            Weight = Vertics_lis[v2.getId()][1] + v2.getWeight(w)
            if w not in Visted:
                Visted.add(w)
                q.enqueue(w)
                Vertics_lis[w.getId()]= [v2.getId(), Weight]
            else:
                if Weight < Vertics_lis[w.getId()][1]:
                    Vertics_lis[w.getId()] = [v2.getId(), Weight]
   List_Short =[]
   for v in g:
       path = []
       weight= 0
       if v.getId() == Target:
           List_Short.append((v.getId(),path,weight))
       else:
            x= find_path(v.getId(),path,weight, Target, Vertics_lis, v.getId())
            List_Short.append(x)
   return List_Short
def find_path(vex, path, weight, Target,Vertice_lis,OG):
    path.append(vex)
    found = Vertice_lis[vex][0]
    if found == Target:
        path.append(found)
        return (OG, path, Vertice_lis[OG][1])
    return find_path(found,path, weight, Target,Vertice_lis, OG)
