class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last_node = self.head.prev

            last_node.next = new_node
            new_node.prev = last_node

            new_node.next = self.head
            self.head.prev = new_node

    def print_list(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

            if current_node == self.head:
                break

circular_doubly_linked_list = CircularDoublyLinkedList()
circular_doubly_linked_list.insert(1)
circular_doubly_linked_list.insert(2)
circular_doubly_linked_list.insert(3)

circular_doubly_linked_list.print_list()
