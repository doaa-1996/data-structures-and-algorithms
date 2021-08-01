class Node:
  def __init__(self, val, next_node = None):
    self.value = val
    self.next = next_node
class Stack:
  def __init__(self, top = None):
    self.top = top

  def push(self, value):
    new_top = Node(value, self.top)
    self.top = new_top

  def pop(self):
    if not isinstance(self.top, Node):
      raise EmptyListError
    removed = self.top
    self.top = self.top.next
    return removed.value

  def peek(self):
    if isinstance(self.top, Node):
      return self.top.value
    raise EmptyListError

  def is_empty(self):
    if self.top:
      return False
    return True

class EmptyListError(AssertionError):
  pass

class Pseudo_Queue:
  def __init__(self):
    self.stack = Stack()

  def enqueue(self, val):
    self.stack.push(val)

  def dequeue(self):
    rev_stack = Stack()
    while self.stack.top:
      rev_stack.push(self.stack.pop())
    removed = rev_stack.pop()
    while rev_stack.top:
      self.enqueue(rev_stack.pop())
    return removed


