import pytest
from stacks_and_queues import __version__

def test_version():
    assert __version__ == '0.1.0'


from stacks_and_queues.stacks_and_queues import Node,Stack, Queue


def test_push():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  assert test_stack.top.value == 2


def test_push1():
  test_stack = Stack()
  test_stack.push(4)
  test_stack.push(5)
  assert test_stack.top.value == 5

def test_push2():
  test_stack = Stack()
  test_stack.push(5)
  test_stack.push(10)
  assert test_stack.top.value == 10

def test_pop():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)
  popped = test_stack.pop()
  assert popped == 3
  assert test_stack.length == 2
  assert test_stack.top.value == 2


def test_pop1():
  test_stack = Stack()
  test_stack.push(6)
  test_stack.push(7)
  test_stack.push(8)
  popped = test_stack.pop()
  assert popped == 8
  assert test_stack.length == 2
  assert test_stack.top.value == 7


def test_pop2():
  test_stack = Stack()
  test_stack.push(10)
  test_stack.push(20)
  test_stack.push(30)
  popped = test_stack.pop()
  assert popped == 30
  assert test_stack.length == 2
  assert test_stack.top.value == 20



def test_peek():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)

  assert test_stack.peek() == 3




def test_peek1():
  test_stack = Stack()
  test_stack.push(10)
  test_stack.push(20)
  test_stack.push(30)

  assert test_stack.peek() == 30


def test_peek2():
  test_stack = Stack()
  test_stack.push(11)
  test_stack.push(12)
  test_stack.push(13)

  assert test_stack.peek() == 13





def test_enqueue():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  assert q.front.value == 1



def test_enqueue1():
  q = Queue()
  q.enqueue(11)
  q.enqueue(22)
  q.enqueue(33)

  assert q.front.value == 11



def test_enqueue2():
  q = Queue()
  q.enqueue(100)
  q.enqueue(200)
  q.enqueue(300)

  assert q.front.value == 100




def test_dequeue():
  q = Queue()
  q.enqueue(111)
  q.enqueue(222)
  q.enqueue(333)
  q.dequeue()

  assert q.length == 2
  assert q.front.value == 222


  


def test_dequeue2():
  q = Queue()
  q.enqueue(8)
  q.enqueue(9)
  q.enqueue(10)
  q.dequeue()

  assert q.length == 2
  assert q.front.value == 9


  

def test_dequeue2():
  q = Queue()
  q.enqueue(30)
  q.enqueue(60)
  q.enqueue(90)
  q.dequeue()

  assert q.length == 2
  assert q.front.value == 60