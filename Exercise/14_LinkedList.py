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

    
    def print_list(self):
        current_node = self.head
        #is not = intervalo fechado de !=, inclui o != 2, = [0,1], is not 2 = [0,1,2]
        while current_node is not None:
            print(current_node.data, end=' -> ')
            #current node assume o valor do ponteiro que aponta para o data do próx nó
            current_node = current_node.next
    
ll1 = LinkedList()
ll1.Insert_Data_beginning(20)
ll1.Insert_Data_end(10)
ll1.Insert_Data_beginning(30)
ll1.print_list()

#Se começar adicionando no final, não tera valor none, pois o head -> none, passara head -> new_node
