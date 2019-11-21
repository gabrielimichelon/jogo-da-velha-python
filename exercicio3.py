import random
import sys
import numpy as np
class Board:
    def __init__(self):
        self.board = np.chararray((3,3))
    
    def board_empty(self):
        self.board[:] = ''
        # print(self.board)
        return self.board
        
    def print_board(self):
        b = self.board_empty()
        print(b)
        

class Node:
    def __init__(self, data):
        self.data = data
        self.nivel = []

    # def __str__(self):
    #     return str(self.data)
    
    def __repr__(self):
        return "{} --> {}".format(self.data, self.nivel)
    
    @property
    def get_data(self):
        return self.data
    
    @property
    def get_nivel(self):
        return self.nivel

class Tree:
    def __init__(self):
        self.root = None
        
    def __repr__(self):
        return "{}".format(self.root)

    def get_root(self):
        return self.root

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, node):
        print("RAIZ {}".format(node))
        print("------->>>> {} <--> {}".format(value, node.data))
        current_root = node.data

        if value is not current_root:
            print("DATA --> {}".format(node.data))
            print("NEXT --> {}".format(node.nivel))
            node.nivel.append(value)
        print("NEXT --> {}".format(node.nivel))
    
    def set_root(self, value):
        if self.root is not value:
            self.root = Node(value)
        
    
    def simetric_transversal(self, node=None):
        if node is None:
            node = self.root
        else:
            print(self.get_root)
            self.simetric_transversal(self.get_root)
        print("{} --> {}".format(tree, node.nivel), end="" )
        # print("({} - {})".format(node, node.nivel), end="")
                   
def menu():
    while list_data:
        print(list_data)
        position = int(input("Qual posição quer inserir?"))
        list_data.remove(position)
        tree.set_root(position)
        for value in list_data:
            tree.insert(value)
            
            # tree.simetric_transversal()      
        # elif op == 2:
        #     for value in aux_list:
        #         tree.set_root(value)
        #     tree.simetric_transversal()
        # print(tree)
    board.print_board()
    print(end="\n")
        # else:
        #     break
    

if __name__ == "__main__":
    tree = Tree()
    board = Board()

    list_data = []
    aux_list = []
    qt = int(input("Quantidade de dados da lista: "))
    for i in range(0, qt+1):
        list_data.append(i)
    print(list_data)
    aux_list = list_data[:]
    for value in list_data:
        tree.insert(value)
    # tree.simetric_transversal()
    list_data.remove(0)
    menu()
    # for value in aux_list:
        # tree.set_root(value)
        # tree.simetric_transversal()
    