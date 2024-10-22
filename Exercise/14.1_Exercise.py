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
        print('\n')

    def Remove_element(self, data):
        current_node = self.head
        previous_node = None

        if current_node is not None and current_node.data == data:
            self.head = current_node.next
            current_node = None

        #Percorre a lista, acha valor, nó anterior aponta para o nó da 'frente' ao valor a ser removido
        while current_node is not None:
            if current_node.data == data:
                #ponteiro anterior aponta para ponteiro pulando o node do current_node
                previous_node.next = current_node.next
                current_node = None
                return
            
            #Pecorre a lista com 1 'memória' do passo anterior 
            previous_node = current_node
            current_node = current_node.next

    def Node_Numbers(self):
        current_node = self.head
        count = 0

        if self.head == None:
            print(count)
            return

        while current_node != None:
            count += 1
            current_node = current_node.next
        print(count)
        return

ll1 = LinkedList()
ll1.Insert_Data_beginning(20)
ll1.Insert_Data_end(30)
ll1.Insert_Data_beginning(10)
ll1.print_list()

''' -> Remove_elemente teste
print('-='*30)
ll1.Remove_element(20)
ll1.Remove_element(10)
ll1.print_list()

ll1.Node_Numbers()
'''