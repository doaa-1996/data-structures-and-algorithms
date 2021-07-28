from hashmap_left_join import __version__


def test_version():
    assert __version__ == '0.1.0'



from hashmap_left_join.hashmap_left_join import left_join

def test1():
    lst1 = ['name', 'age']
    lst2 = ['doaa', '24']
    lst3 = ['name', 'age']
    lst4 = ['dana', '14']

    map_a = dict(zip(lst1, lst2))

    map_b = dict(zip(lst3, lst4))

    left_join(map_a, map_b)
    assert left_join(map_a, map_b)==[['name', 'doaa', 'dana'], ['age', '24', '14']]




def test2():
    lst1 = ['x', 'y']
    lst2 = ['a', 'b']
    lst3 = ['x', 'y']
    lst4 = ['c', 'd']

    map_a = dict(zip(lst1, lst2))

    map_b = dict(zip(lst3, lst4))

    left_join(map_a, map_b)
    assert left_join(map_a, map_b)==[['x', 'a', 'c'], ['y', 'b', 'd']]    