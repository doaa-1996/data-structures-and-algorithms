from linked_list import __version__
import linked_list
from linked_list.linked_list import LinkedList, Node


def test_version():
    assert __version__ == '0.1.0'


def test_Node():
    a = Node(5)
    assert a.value is 5
    assert a.next is None


def test_append_1():
    ll = LinkedList()
    ll.append(1)
    assert ll.head.value is 1
    ll.append(2)
    assert ll.head.next.value is 2
    assert ll.head.next.next is None


def test_insert():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value is 5
    assert ll.head.next is None
    ll.insert('s')
    assert ll.head.value is 's'
    assert ll.head.next.value is 5
    ll.append('i')
    assert ll.head.value is 's'
    assert ll.head.next.value is 5
    ll.insert(17)
    assert ll.head.value is 17
    assert ll.head.next.value is 's'


def test_include():
    ll = LinkedList()
    assert ll.include(0) is False
    ll.append(2)
    assert ll.include(6) is False
    assert ll.include(2) is True
    ll.append(7)
    ll.insert(8)
    assert ll.include(11) is False
    assert ll.include(5) is False
    assert ll.include(7) is True
    assert ll.include(8) is True
    ll.insert(88)
    ll.append(3)
    assert ll.include(88) is True
    assert ll.include(3) is True
    assert ll.include(6) is False


def test_include1():
    ll = LinkedList()
    assert ll.include(0) is False
    ll.append(10)
    assert ll.include(10) is True


def test_str():
    ll = LinkedList()
    assert str(ll) is 'None'
    ll.append(5)
    assert str(ll) == '{ 5 } -> None'
    ll.append(5)
    assert str(ll) == '{ 5 } -> { 5 } -> None'
    ll.append(4)
    ll.insert(3)
    ll.append(2)
    assert str(ll) == '{ 3 } -> { 5 } -> { 5 } -> { 4 } -> { 2 } -> None'


def test_insertBefore():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insertBefore(2, 20)
    assert ll.head.next.value == 20
    ll.insertBefore(20, 44)
    assert ll.head.next.value == 44


def test2():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insertBefore(2, 20)
    ll.insertBefore(20, 44)
    assert ll.head.next.value == 44


def test3():
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.append(8)
    ll.insertBefore(8,10)
    assert ll.head.next.next.value==10



def test_insertAfter():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insertAfter(1, 30)
    assert ll.head.next.value == 30



def test_insertAfter():
    ll = LinkedList()
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insertAfter(5, 3)
    assert ll.head.next.next.value == 3



def test_insertAfter():
    ll = LinkedList()
    ll.append(2)
    ll.append(5)
    ll.append(9)
    ll.insertAfter(9, 3)
    assert ll.head.next.next.next.value == 3

