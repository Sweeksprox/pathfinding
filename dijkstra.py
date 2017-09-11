from collections import deque
import time
import math

class Node:
	def __init__(self, name):
		self.name = name
		self.paths = {}
		self.pathTo = []
		self.last = None
		self.value = float('inf')

	def addPath(self, node, value):
		self.paths[node] = value

class PriorityQueue:
	def __init__(self):
		self.queue = []

	def __len__(self):
		return len(self.queue)

	def __getitem__(self, item):
		return self.queue[item]

	def __setitem__(self, item, val):
		self.queue[item] = val

	def enqueue(self, node):
		self.queue.append(node)

	def dequeue(self, node):
		self.queue.remove(node)

	def popleft(self):
		return self.queue.pop(0)

	def reorder(self):
		for i in range(len(self.queue)):
			for j in range(len(self.queue) - 1 - i):
				if self.queue[j].value > self.queue[j + 1].value:
					self.queue[j], self.queue[j + 1] = self.queue[j + 1], self.queue[j]

def solve(end, queue):
	visited = []
	while True:
		queue.reorder()
		item = queue.popleft()
		visited.append(item)
		for n in item.paths:
			if n not in visited:
				if n.value > item.paths[n] + item.value:
					n.value = item.paths[n] + item.value
					n.last = item
				if n not in queue:
					queue.enqueue(n)
				if n == end:
					n.last = item
					return

def printPath(node):
	if node.last != None:
		print(node.last.name)
		printPath(node.last)

s = Node('s')
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

s.addPath(a, 5)
s.addPath(d, 4)
s.value = 0

a.addPath(s, 5)
a.addPath(b, 2)
a.addPath(c, 1)

b.addPath(a, 2)
b.addPath(f, 1)

c.addPath(a, 1)
c.addPath(f, 2)

d.addPath(c, 4)
d.addPath(e, 16)

e.addPath(d, 2)
e.addPath(f, 3)

f.addPath(b, 1)
f.addPath(c, 2)
f.addPath(e, 3)

queue = PriorityQueue()
queue.enqueue(s)
queue.enqueue(a)
queue.enqueue(b)
queue.enqueue(c)
queue.enqueue(d)
queue.enqueue(e)
queue.enqueue(f)

time1 = time.clock()
solve(f, queue)
time2 = time.clock()

printPath(f)
print('Time: ' + str(time2 - time1))