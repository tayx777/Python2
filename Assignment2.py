# Removing a Node from a Singly Linked List
# ====================================
# Task: Implement a method  remove(data) in the  LinkedList class that removes the first occurrence of a node
# with the specified data from the list.



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(24)
ll.append(3)
ll.append(2)
ll.append(4)

print("Original list:", ll.display())
ll.remove(2)
print("After removing 2:", ll.display())
ll.remove(4)
print("After removing 4:", ll.display())
ll.remove(1)
print("After removing 1:", ll.display())
ll.remove(5)
print("After trying to remove 5 (not in list):", ll.display())