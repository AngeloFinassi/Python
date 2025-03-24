from typing import Optional

class ListNode:
    def __init__(self, val=0):  #Corrigi 'data' para 'val', padrão do LeetCode
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        bummy = ListNode()  #nó fictício
        # current é o ponteiro que percorre list1 e list2 e dps vai adicionando em bunny dps de trabalhar com os valores
        current = bummy  

        while list1 and list2:
            if list1.val < list2.val:  #referencia o nó do current para o nó list1, n pega o valor, só aponta
                current.next = list1  
                list1 = list1.next  #lista avança um passo
            
            else:
                #current referencia a lista
                current.next = list2  
                #lista avança um passo
                list2 = list2.next  

            current = current.next  #Avança o ponteiro current para crescer a lista

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return bummy.next  #retorna a cabeça da lista
