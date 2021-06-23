from ll_zip import __version__


def test_version():
    assert __version__ == '0.1.0'

from ll_zip.ll_zip import Node,zipLists,printList



def test_llzip1():
    a = b = None
    for i in reversed(range(7, 12, 2)):
        a = Node(i, a)

    for i in reversed(range(2, 7, 2)):
        b = Node(i, b) 

    zippedlist = zipLists (a, b)    
    assert printList("",zippedlist)=='7 —> 2 —> 9 —> 4 —> 11 —> 6 —> None'






def test_llzip2():
    a = b = None
    for i in reversed(range(1, 6, 2)):
        a = Node(i, a)

    for i in reversed(range(2, 7, 2)):
        b = Node(i, b) 

    zippedlist = zipLists (a, b)    
    assert printList("",zippedlist)=='1 —> 2 —> 3 —> 4 —> 5 —> 6 —> None'





def test_llzip3():
    a = b = None
    for i in reversed(range(1, 3, 1)):
        a = Node(i, a)

    for i in reversed(range(2, 5, 1)):
        b = Node(i, b) 

    zippedlist = zipLists (a, b)    
    assert printList("",zippedlist)=='1 —> 2 —> 2 —> 3 —> 4 —> None'
