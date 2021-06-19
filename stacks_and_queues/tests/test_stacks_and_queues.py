import pytest
from stacks_and_queues import __version__

def test_version():
    assert __version__ == '0.1.0'


from stacks_and_queues.stacks_and_queues import  Stack, Queue, PseudoQueue




def test_push(stack_3_vals):

    assert stack_3_vals.top.value == 'd'

def test_pop(stack_3_vals):

    assert stack_3_vals.pop() == 'd'
    assert stack_3_vals.top.value == -7
    assert stack_3_vals.pop() == -7
    assert stack_3_vals.pop() == 3


def test_peek(stack_3_vals):

    assert stack_3_vals.peek() == 'd'
    assert stack_3_vals.top.value == 'd'



def test_is_empty(stack_3_vals):

    assert stack_3_vals.isEmpty() == False



def test_enqueue(queue_vals):

    q = Queue()
    assert q.front == None
    assert q.rear == None

    q.enqueue(2)
    assert q.front.value == 2
    assert q.rear.value == 2

    q.enqueue(10)
    assert q.front.value == 2
    assert q.rear.value == 10

    assert queue_vals.rear.value == 6
    assert queue_vals.front.value == 8



def test_peek(queue_vals):
    q = Queue()
    assert queue_vals.peek() == 8

def test_is_empty(queue_vals):
    q = Queue()
    assert q.isEmpty() == True
    assert queue_vals.isEmpty() == False


def test_dequeue():
  q = PseudoQueue()
  q.enqueue(1)
  q.enqueue(2)
  q.enqueue(3)

  popped = []
  for _ in range(3):
    popped.append(q.dequeue())
  
  assert popped == [1, 2, 3]

@pytest.fixture
def stack_3_vals():
    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    return stack

@pytest.fixture
def queue_vals():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue