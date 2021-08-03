class Vertex:
    def __init__(self,value):
        self.value = value
class Edge:
    def __init__(self,node,weight):
        self.node = node
        self.weight = weight
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_node(self,value):
        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex
    def add_edge(self,node1, node2, weight=0):
        try:
            if not node1 in self.adjacency_list.keys():
                raise Exception
            self.adjacency_list[node1].append(Edge(node2,weight))
        except:
            return 'either node 1 or node 2 does not exits'
    def get_nodes(self):
        if len(self.adjacency_list.keys()):
            return list(self.adjacency_list.keys())
        return None
    def get_neighbors(self,node):
        return self.adjacency_list[node]
    def size(self):
        return len(self.adjacency_list.keys())
    def breadth_first(self,node):
        try:
            if not node in self.adjacency_list.keys():
                raise Exception
            all = []
            breadth = []
            all.append(node)
            breadth.append(node)
            while(len(all)):
                edges = self.get_neighbors(node)
                if len(edges):
                    for edge in edges:
                        if not (edge.node in all) and not (edge.node in breadth):
                            all.append(edge.node)
                breadth.append(all.pop(0))
                if len(all):
                    node = all[0]
            breadth.pop(0)
            return breadth
        except:
            return "this node is not one of this graph's vertexes"
   
    

def business_trip(graph, array):
  counter = 0
  bool = True
  all_nodes = graph.get_nodes()
  if len(array)<2:
    return 'False, $0'
  new_array = []
  for item in array:
    for node in all_nodes:
      if item == node.value:
        new_array.append(node)
        continue
  if len(array) != len(new_array):
    return None

  def route (value, next_value):
    nonlocal counter,bool, new_array
    if not bool:
      return

    edges = graph.get_neighbors(value)
    if not len(edges):
      bool = False
      return
    for edge in edges:
      if next_value == edge.node:
        counter += edge.weight
        break
    else:
      bool = False
      return
    new_array.pop(0)
    if len(new_array)<2:
      return
    route(new_array[0], new_array[1])

  route(new_array[0], new_array[1])
  if bool:
    return f'{bool}, ${counter}'

  return f'{bool}, $0'
        

