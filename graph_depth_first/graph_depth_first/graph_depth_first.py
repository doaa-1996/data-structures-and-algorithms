from collections import deque

class Graph:

  def __init__(self):
   
    self._adjacency_list = {}

  def add(self, value):

    v = Vertex(value)
    self._adjacency_list[v] = []
    return v

  def add_edge(self, start, end, weight=0):
   
    self.__valid_vertex(start)
    self.__valid_vertex(end)

    for edge in self._adjacency_list[start]:

      if edge == (end, int):
        edge = (end, weight)
        return

    self._adjacency_list[start].append((end, weight))


  def size(self):
    return len(self._adjacency_list)


  def get_vertices(self):
    return list(self._adjacency_list.keys())


  def get_neighbors(self, vertex):
    self.__valid_vertex(vertex)
    return self._adjacency_list[vertex]


 


  def depth_first(self, vertex):
   
    output = []

    def action(vertex):
      output.append(vertex.value)

    self.__recurse(vertex, action)

    return output


  def add_double_edge(self, vertex1, vertex2, weight=0, weight2=None):
    
    weight2 = weight if weight2 == None else weight2 or 0
    self.add_edge(vertex1, vertex2, weight)
    self.add_edge(vertex2, vertex1, weight2)





  def __recurse(self, vertex, action):
    
    visited = set()

    def recurse(vertex, action):

      visited.add(vertex)
      action(vertex)

      for vert in self.get_neighbors(vertex):
        if vert[0] not in visited:
          recurse(vert[0], action)

    recurse(vertex, action)


  def __valid_vertex(self, vertex):
   
    if vertex not in self._adjacency_list.keys():
      raise KeyError(f'Vertex {vertex} is not in graph')
    return True


  def __len__(self):
    return len(self._adjacency_list)


class Vertex:
  

  def __init__(self, value):
    self.value = value

  def __str__(self):
    return self.value



class Stack:
  def __init__(self):
    self.dq = deque()

  def push(self, value):
    self.dq.append(value)

  def pop(self):
    return self.dq.pop()

  def empty(self):
    return len(self.dq) == 0