# middle_node.py
# Problem: https://leetcode.com/problems/middle-of-the-linked-list/
# Category: Linked List
# Difficulty: Easy

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """Append a new node to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle_node(self):
        """
        Finds the middle node using the two-pointer technique.
        If there are two middle nodes, returns the second one.
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    for value in [2, 3, 4, 5]:
        ll.append(value)

    middle = ll.find_middle_node()
    print(f"Middle Node: {middle}")
