class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        current_node = self.head
        count = 0

        # Se a lista estiver vazia ou índice inválido
        if self.head is None:
            return -1

        # Percorre a lista até encontrar o índice
        while current_node is not None and count != index:
            count += 1
            current_node = current_node.next

        # Se o índice for maior que o tamanho da lista
        if current_node is None:
            return -1

        return current_node.data

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def addAtIndex(self, index, val):
        new_node = Node(val)

        # Caso especial: inserir no início (índice 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        previous_node = None
        count = 0

        # Percorre a lista até encontrar o índice
        while current_node is not None and count != index:
            count += 1
            previous_node = current_node
            current_node = current_node.next

        # Se o índice for maior que o tamanho da lista, não insere
        if count != index:
            return

        # Inserção no meio da lista
        previous_node.next = new_node
        new_node.next = current_node

    def deleteAtIndex(self, index):
        current_node = self.head

        # Caso especial: deletar o primeiro nó (índice 0)
        if index == 0 and current_node is not None:
            self.head = current_node.next  # Atualiza o head
            current_node = None  # Libera o nó
            return

        previous_node = None
        count = 0

        # Percorre a lista até encontrar o índice
        while current_node is not None and count != index:
            count += 1
            previous_node = current_node
            current_node = current_node.next

        # Se o índice for maior que o tamanho da lista, não deleta
        if current_node is None:
            return

        # Remover o nó atual
        previous_node.next = current_node.next
        current_node = None

ll = MyLinkedList()
ll.addAtHead(10)
ll.addAtTail(20)
ll.addAtTail(30)
print(ll.get(1))  # Deve retornar 20
ll.addAtIndex(1, 15)
print(ll.get(1))  # Deve retornar 15
ll.deleteAtIndex(2)
print(ll.get(2))  # Deve retornar 30