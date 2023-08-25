class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.prev = current_node

    def reverse(self):
        current_node = self.head

        while current_node:
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            current_node = current_node.prev

        if temp:
            self.head = temp.prev

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert(1)
doubly_linked_list.insert(2)
doubly_linked_list.insert(3)

doubly_linked_list.print_list()

doubly_linked_list.reverse()

doubly_linked_list.print_list()
