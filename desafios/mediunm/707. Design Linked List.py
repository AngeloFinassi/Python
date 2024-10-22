#ESSE AQUI DEU ORGULHO kkkkkkk
class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def Insert_Data_beginning(self, data):
        new_node = Node(data)
        #ponteiro do new_node aponta para o valor que o head apontava
        new_node.next = self.head
        #head aponta para new_node
        self.head = new_node
        #head -> new_node -> None

    def Insert_Data_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def get(self, index):
        current_node = self.head
        count = 0

        if self.head == None:
            index = None
            return

        while count != index:
            count += 1
            current_node = current_node.next
        count = index
        return current_node.data

    def addAtIndex(self, index, val):
        new_node = Node(val)

        #Caso especial:inserir no ínicio (indice 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        previous_node = None
        count = 0

        while current_node != None:
            #Ao chegar na posição new_node aponta para o atual, o antigo aponta para o new node, o atual continua apontando para o da frente
            if count == index:
                previous_node.next = new_node
                new_node.next = current_node
                return

            count += 1
            previous_node = current_node
            current_node = current_node.next

        # Insere no final da lista
        if count == index:
            previous_node.next = new_node

    def deleteAtIndex(self, index):
        current_node = self.head
        previous_node = None
        count = 0

        while current_node != None:
            #Ao chegar na posição previous_node -> current_node.next
            if count == index:
                previous_node.next = current_node.next
                current_node = None
                return

            count += 1
            previous_node = current_node
            current_node = current_node.next

ll = MyLinkedList()
ll.addAtHead(10)
ll.addAtTail(20)
ll.addAtTail(30)
print(ll.get(1))  # Deve retornar 20
ll.addAtIndex(1, 15)
print(ll.get(1))  # Deve retornar 15
ll.deleteAtIndex(2)
print(ll.get(2))  # Deve retornar 30