from graph_breadth_first import __version__
from graph_breadth_first.graph_breadth_first import Graph
def test_version():
    assert __version__ == '0.1.0'


def test1():
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,4)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,2)
    assert g.BFS(1)== [1, 4, 0, 2, 3, 5]



def test2():
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(1,4)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,2)
    assert g.BFS(0)== [0, 1, 2, 3, 4, 5]



