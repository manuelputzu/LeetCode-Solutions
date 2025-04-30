# middle_node.py
# Problem: https://leetcode.com/problems/middle-of-the-linked-list/
# Category: Linked List
# Difficulty: Easy

class Node:
    def __init__(self, value=0, next=None):
        # Each node holds a value and a reference to the next node
        self.value = value
        self.next = next

    def __str__(self):
        # When printing a Node, only show its value
        return str(self.value)


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list
        self.head = None  # First node
        self.tail = None  # Last node
        self.length = 0   # Number of nodes in the list

    def __str__(self):
        # Return a string representation of the entire list
        values = []
        current = self.head
        while current:
            values.append(str(current.value))  # Use str to call Node.__str__()
            current = current.next
        return " -> ".join(values)  # Example: "1 -> 2 -> 3"

    def append(self, value):
        # Create a new node and add it to the end of the list
        new_node = Node(value)
        if self.length == 0:
            # If the list is empty, set head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, add the node at the end and update the tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def find_middle_node(self):
        # Use the fast and slow pointer method to find the middle node
        slow = self.head
        fast = self.head

        # Move 'fast' by 2 and 'slow' by 1 step until 'fast' reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When the loop ends, 'slow' is at the middle
        return slow

# Example usage:
if __name__ == "__main__":
    my_list = LinkedList()

    # Append values to the linked list
    for i in [1, 2, 3, 4]:
        my_list.append(i)

    # Find the middle node
    middle = my_list.find_middle_node()

    # Print the entire list
    print(my_list)

    # Print the value of the middle node
    print(f"Middle Node: {middle}")
