class Stack:
  def __init__(self, collection=None):
    self.top = None
    if collection:
      for item in reversed(collection):
        self.insert(item)

  def insert(self, value):
    self.top = Node(value, self.top)

  def __iter__(self):
    def value_generator():
      current = self.top
      while current:
        yield current.value
        current = current.next
    return value_generator()

  def __len__(self):
    return len(list(iter(self)))


class Node:
  def __init__(self, value, next_ = None):
    self.value = value
    self.next = next_