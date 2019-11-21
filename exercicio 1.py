import numpy as np
from numpy.random.mtrand import rand, randint


class Matrix:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.matrix = np.zeros((x, y))

    def fill(self):
        for i in range(0, self.x):
            for j in range(0, self.y):
                self.matrix[i,j] = randint(100)
        print(self.matrix)
        return (self.matrix)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return "{} -> {}".format(self.data, self.next)

    @property
    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    @property
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:

    def __init__(self):
        self.head = None
        
    def __repr__(self):
        return "[{}]".format(self.head)

    def add(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node
        print("Dado inserido na lista: {}".format(node.get_data))
    
    def search(self, data):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data == data:
                found = True
            else:
                current = current.get_next
        return found
    
x = int(input("Insira quantas linhas: "))
y = int(input("Insira quantas colunas: "))

mat = Matrix(x, y)
aux_matrix = mat.fill()
linked_list = LinkedList()

for i in range(0, x):
    for j in range(0, y):
        linked_list.add(aux_matrix[i,j])

print(linked_list)