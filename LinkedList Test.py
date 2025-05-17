from random import random, Random


class Node:
  def __init__(self, value):
    self.data = value
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self._size = 0
    self._head = None
    self._tail = None

  def pushBack(self, value):
    node = Node(value)
    self._size = self._size + 1
    if self._head is None:
      self._head = node
      self._tail = node
      return
    self._tail.next = node
    self._tail = node

  def popBack(self):
    self._size = self._size - 1
    if self._head.next is None:
      self._head = None
      self._tail = None
      return
    current = self._head
    while current.next != self._tail:
      current = current.next
    current.next = None
    self._tail = current

  def pushFront(self, value):
    node = Node(value)
    self._size = self._size + 1
    if self._head is None:
      self._head = node
      self._tail = node
      return
    node.next = self._head
    self._head = node

  def popFront(self):
    self._size = self._size - 1
    self._head = self._head.next
    if self._head is None:
      self._tail = None

  def front(self):
    return self._head.data

  def back(self):
    return self._tail.data

  def size(self):
    return self._size


def testPushBack():
  l = LinkedList()
  l.pushBack(7)
  assert l.back() == 7
  assert l.front() == 7
  l.pushBack(3)
  assert l.back() == 3
  assert l.front() == 7
  l.pushBack(300)
  assert l.back() == 300
  assert l.front() == 7

def testPushFront():
  l = LinkedList()
  l.pushFront(7)
  assert l.back() == 7
  assert l.front() == 7
  l.pushFront(3)
  assert l.back() == 7
  assert l.front() == 3
  l.pushFront(300)
  assert l.back() == 7
  assert l.front() == 300

def testPopBack():
  l = LinkedList()
  l.pushBack(5)
  l.pushBack(3)
  l.pushBack(10)
  assert l.back() == 10
  assert l.front() == 5
  l.popBack()
  assert l.back() == 3
  assert l.front() == 5
  l.popBack()
  assert l.back() == 5
  assert l.front() == 5
  l.popBack()
  l.pushFront(1000)
  assert l.back() == 1000
  assert l.front() == 1000

def testPopFront():
  l = LinkedList()
  l.pushBack(5)
  l.pushBack(3)
  l.pushBack(10)
  assert l.back() == 10
  assert l.front() == 5
  l.popFront()
  assert l.back() == 10
  assert l.front() == 3
  l.popFront()
  assert l.back() == 10
  assert l.front() == 10
  l.popBack()
  l.pushFront(1000)
  assert l.back() == 1000
  assert l.front() == 1000

random = Random()

def pushTest(l, arr, num_operations):
  for i in range(num_operations):
    x = random.randint(0, 10000)

    if random.randint(0, 2) == 0:
      l.pushBack(x)
      arr.append(x)
    else:
      l.pushFront(x)
      arr.insert(0, x)

    assert arr[0] == l.front()
    assert arr[-1] == l.back()
    assert len(arr) == l.size()

  return l, arr


def popTest(l, arr, num_operations):
  for i in range(100):
    if random.randint(0, 2) == 0:
      arr.pop()
      l.popBack()
    else:
      arr = arr[1:]
      l.popFront()

    assert arr[0] == l.front()
    assert arr[-1] == l.back()
    assert len(arr) == l.size()

  return l, arr


def randomTest():

  l = LinkedList()
  arr = []

  l, arr = pushTest(l, arr, 200)
  l, arr = popTest(l, arr, 100)
  l, arr = pushTest(l, arr, 100)
  l, arr = popTest(l, arr, 200)


testPushBack()
testPushFront()
testPopBack()
testPopFront()
randomTest()

print ("Everything should be fine if you see this")