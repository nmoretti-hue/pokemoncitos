class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SingleLink:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def link_nodes(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
 
    def insert_node(self, node, pos):
        cant = 0
        current = self.head
        while cant < pos:
            current = current.next
            prev_current = current.prev
            cant += 1
        prev_current.next = node
        node.next = current
    
    def travel_list(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
        exit()

    def search_data(self, data):
        pos = 0
        current = self.head
        while current != None:
            if data == current.data:
                print(f"la data esta en el nodo {pos}")
                exit()
            else:
                print(f"{current.data}")
                pos += 1
                current = current.next
        print("no esta la data en el nodo")
    
    def len_list(self):
        cant = 0
        current = self.head
        while current != None:
            cant += 1
            current = current.next
        print(f"largo de la lista = {cant}")
    
    def delete_node(self, data):
        pos = 0
        current = self.head
        
        while current != None:
            next_node = current.next
            prev_node = current.prev
            if data == current.data:
                next_node.prev = prev_node
                prev_node.next = next_node
                current.next = None
                current.prev = None
                lista.travel_list()
            else:
                current = current.next
        print("no esta la data")

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
    
    def sort_list(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None

        current = self.head
        while current:
            next_node = current.next

            current.prev = current.next = None

            if sorted_head is None:
                sorted_head = current
            else:
                if current.data < sorted_head.data:
                    current.next = sorted_head
                    sorted_head.prev = current
                    sorted_head = current
                else:
                    temp = sorted_head
                    while temp.next and temp.next.data < current.data:
                        temp = temp.next

                    current.next = temp.next
                    if temp.next:
                        temp.next.prev = current
                    temp.next = current
                    current.prev = temp

            current = next_node

    
        self.head = sorted_head

        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp

lista = SingleLink()