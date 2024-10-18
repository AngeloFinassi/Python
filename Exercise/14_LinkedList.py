class Node:
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Inicialmente, não há próximo nó

class LinkedList:
    def __init__(self):
        self.head = None  # Inicialmente, a lista está vazia (sem cabeça)

    #Inserção Início
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)  # Cria um novo nó com os dados
        new_node.next = self.head  # O novo nó aponta para o atual primeiro nó
        self.head = new_node  # O novo nó agora é o primeiro (head)

    #Inserção Final
    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:  # Se a lista está vazia, o novo nó será o head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Percorre até o último nó
            last = last.next
        last.next = new_node  # O último nó agora aponta para o novo nó

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")  # Indica o fim da lista

# Criando uma lista vazia
llist = LinkedList()

# Inserindo elementos
llist.insert_at_beginning(10)
llist.insert_at_beginning(20)
llist.insert_at_end(30)

# Exibindo a lista
llist.print_list()
