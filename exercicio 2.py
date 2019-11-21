import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

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
        if value < node.data:
            print("DATA < {}".format(node.data))
            print("LEFT < {}".format(node.left))
            print("RIGHT < {}".format(node.right))
            if node.left is not None:
                self._insert(value, node.left)
                node.left.parent = node
                print("Left -> ", node.left)
            else:
                node.left = Node(value)
                print("Left -> ", node.left)
        else:
            if node.right is not None:
                self._insert(value, node.right)
                node.right.parent = node
                print("Right -> ", node.right)
            else:
                node.right = Node(value)
                print("Right -> ", node.right)

    def simetric_transversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.simetric_transversal(node.left)
        if node.right:
            self.simetric_transversal(node.right)
        print("({} - {} - {})".format(node.left, node, node.right), end="")


def menu(op):
    while op is not 3:
        print("################################")
        print("#######Escolha uma Opção:#######")
        print("#-->1: Inserir lista na árvore #")
        print("#-->2: Ordem na árvore #####")
        print("#-->3: Sair ####################")
        op = int(input("--> "))

        if op == 1:
            print("Inserindo...")
            for value in list_data:
                tree.insert(value)
        elif op == 2:
            pass
            tree.simetric_transversal()
            print(end="\n")
        elif op is 3:
            break


if __name__ == "__main__":
    tree = Tree()

    op = 0

    list_data = []
    qt = int(input("Quantidade de dados da lista: "))
    for i in range(0, qt):
        val = random.randrange(100)
        list_data.append(val)
    print(list_data)
    menu(op)
