from sys import argv
from stack_array import *

class Vertex:
    def __init__(self,degree,av):
        '''Add whatever parameters/attributes are needed'''
        self.degree = degree
        self.av = av

def tsort(vertices):
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * one vertex per line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message 
    *     "input contains a cycle"'''
    if vertices == []:
        raise ValueError('input contains no edges')
    if len(vertices) % 2 != 0:
        raise ValueError('input contains an odd number of tokens')
    dic = {}
    for i in range(0,len(vertices),2):
        V = vertices[i]
        AV = vertices[i+1]
        if V not in dic:
            dic[V] = Vertex(0,[])
        dic[V].av.append(AV)
        if AV not in dic:
            dic[AV] = Vertex(1,[])
        else:
            dic[AV].degree +=1
    stack = Stack (len(vertices))
    for val in vertices:
        if dic[val].degree == 0:
            stack.push(val)
    visited = set()
    order_list = []
    while not stack.is_empty():
        item = stack.pop()
        if item not in visited:
            visited.add(item)
            for val in dic[item].av:
                dic[val].degree -= 1
                if dic[val].degree == 0:
                    stack.push(val)
            order_list.append(item)

    if len(order_list) != len(dic):
        raise ValueError('input contains a cycle')
    return '\n'.join(order_list)



# 100% Code coverage NOT required
def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG.  Use this code 
       if you want to run tests on a file with a list of edges'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()
    
    vertices = []
    for line in f:
        vertices += line.split()
       
    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)
    
if __name__ == '__main__': 
    main()
