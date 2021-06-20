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


def test_pop():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)
  popped = test_stack.pop()
  assert popped == 3
  assert test_stack.length == 2
  assert test_stack.top.value == 2




def test_peek():
  test_stack = Stack()
  test_stack.push(1)
  test_stack.push(2)
  test_stack.push(3)

  assert test_stack.peek() == 3

def test_enqueue():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  assert q.front.value == 1





def test_dequeue():
  q = Queue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)
  q.dequeue()

  assert q.length == 2
  assert q.front.value == 2