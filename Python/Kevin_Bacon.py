from Shortest_path import *
class Node:
    def __init__(self, name):
        self.name = name
        self.edge = []

g = Graph()
N = Node("Kevin Bacon")
N.edge= ["Apollo 13", "Animal House", "The Woodsman", "Wild Things", "The River Wild"]
g.addVertex(N)
N = Node("John Belushi")
N.edge =["Animal House"]
g.addVertex(N)
N = Node("Donal Sutherland")
N.edge =["Animal House", "The Eagle Has Landed", "Cold Mountain", "An American Haunting"]
g.addVertex(N)
N = Node("Kathleen Quinlan")
N.edge =["Apollo 13"]
g.addVertex(N)
N = Node("Tom Hanks")
N.edge =["Apollo 13", "The Da Vinci Code", "Joe Versus the Volcano"]
g.addVertex(N)
N= Node("Serretta Wilson")
N.edge = ["The Da Vinci Code"]
g.addVertex(N)
N= Node("Shane Zaza")
N.edge = ["The Da Vinci Code"]
g.addVertex(N)
N= Node("Yves Aubert")
N.edge = ["The Da Vinci Code"]
g.addVertex(N)
N= Node("Paul Herbert")
N.edge = ["The Da Vinci Code", "Titanic"]
g.addVertex(N)
N= Node("Kate Winslet")
N.edge = ["Titanic", "Eternal Sunshine, of the Spotless Man", "Jude", "Enigma", "Hamlet"]
g.addVertex(N)
N= Node("Merly Streep")
N.edge = ["The River Wild"]
g.addVertex(N)
N= Node("Vernon Dobtcheff")
N.edge = ["Jude", "Murder on the Orient Express", "An American Haunting"]
g.addVertex(N)
N= Node("John Gielgud")
N.edge = ["Hamlet", "Murder on the Orient Express", "Caligola", "Portrait of a Lady"]
g.addVertex(N)
N= Node("Glenn Close")
N.edge = ["The Stepford Wives"]
g.addVertex(N)
N= Node("Nicole Kidman")
N.edge = ["Portrait of a Lady", "The Stepford Wives", "Cold Mountain"]
g.addVertex(N)
N= Node("Patrick Allen")
N.edge = ["Caligola", "The Eagle Has Landed"," Dial M for Murder"]
g.addVertex(N)
N= Node("Grace Kelly")
N.edge = ["Dial M for Murder", "To Catch a Thief", "High Noon"]
g.addVertex(N)
N= Node("Lloyd Bridges")
N.edge = ["High Noon", "Joe Versus the Volcano"]
g.addVertex(N)

for first in g.vertList:
    edge = first.edge
    for Second in g.vertList:
        edge2 = Second.edge
        if edge != edge2:
            for k in range(len(edge)):
                if edge[k] in edge2:
                    g.addEdge(first,Second, 1)
                    break
for v in g:
   for w in v.getConnections():
       print("( %s , %s )" % (v.getId().name, w.getId().name))

def find_Bacon_Num(Name):
    for val in g.vertList:
        x= None
        if val.name == "Kevin Bacon":
            x = shortest_path(val, g)
            break
    if x == None:
        raise ValueError("Kevin Not in Graph")
    for val2 in x:
        if val2[0].name == Name:
            return val2[2]
    raise ValueError("Actor not in Graph")
def find_max_Bacon_Num():
    max = 0
    Actor = None
    for val in g.vertList:
        if val.name != "Kevin Bacon":
            x = find_Bacon_Num(val.name)
            if x > max:
                max = x
                Actor = val.name
    return Actor
def find_min_link(name, name2):
    for val in g.vertList:
        x= None
        if val.name == name:
            x = shortest_path(val, g)
            break
    if x == None:
        raise ValueError("Actor1 Not in Graph")
    for val2 in x:
        if val2[0].name == name2:
            return val2[2]
    raise ValueError("Actor2 not in Graph")

