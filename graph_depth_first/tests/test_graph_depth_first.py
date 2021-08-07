from graph_depth_first import __version__

from graph_depth_first.graph_depth_first import *

def test_version():
    assert __version__ == '0.1.0'

import pytest


def create_sample():
  g = Graph()

  vert_a = g.add('a')
  vert_b = g.add('b')
  vert_c = g.add('c')
  vert_d = g.add('d')
  vert_e = g.add('e')
  vert_f = g.add('f')
  vert_g = g.add('g')
  vert_h = g.add('h')

  g.add_double_edge(vert_a, vert_b)
  g.add_double_edge(vert_a, vert_d)
  g.add_double_edge(vert_b, vert_c)
  g.add_double_edge(vert_b, vert_d)
  g.add_double_edge(vert_c, vert_g)
  g.add_double_edge(vert_d, vert_e)
  g.add_double_edge(vert_d, vert_h)
  g.add_double_edge(vert_d, vert_f)
  g.add_double_edge(vert_f, vert_h)

  return (g, vert_a)

####################
## Test Traversal ##
####################

def test_depth_first_single_value():
  g = Graph()
  vert_a = g.add('a')
  assert g.depth_first(vert_a) == ['a']

def test_one_way_edge_depth_first():
  g = Graph()
  vert_a = g.add('a')
  vert_b = g.add('b')
  g.add_edge(vert_a, vert_b)
  assert g.depth_first(vert_a) == ['a', 'b']
  assert g.depth_first(vert_b) == ['b']

def test_challenge_sample():
  sample = create_sample()
  graph = sample[0]
  root = sample[1]

  assert root.value == 'a'
  assert graph.depth_first(root) == ['a','b','c','g','d','e','h','f']


def test_import():
  g = Graph()
  assert g.add_double_edge