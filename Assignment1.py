# Task: Implement a singly linked list class with the following methods:
# append(data): Adds a new node with the specified data at the end of the list.
# prepend(data): Adds a new node with the specified data at the beginning of the list.
# print_list(): Prints all the elements in the list.


class Node:
    def __init__(self, data):
        self.data = data # store the data
        self.next = None # pointer to the next node

class SinglyLinkedList:
    def __init__(self):
        self.head = None # Initialize the head of the list
    def append(self, data):
        new_node = Node(data) # Create the node
        if not self.head: # If the list is empty, then...
            self.head = new_node # will set the new node as the head
            return
        last_node = self.head
        while last_node.next: # Traverse to the end of the list
            last_node = last_node.next
        last_node.next = new_node # link last node to the new node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head # Link the new node to the current head
        self.head = new_node # Update the head to the new node
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    linkedlist = SinglyLinkedList()

    linkedlist.append(10)
    linkedlist.append(20)
    linkedlist.prepend(5)
    linkedlist.append(15)
    linkedlist.prepend(30)
    linkedlist.print_list()