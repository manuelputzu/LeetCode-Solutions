# kth_node_from_end.py
# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Category: Linked List
# Difficulty: Medium

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


def find_kth_from_end(ll, k):
    
    #Use the two-pointer technique to retrieve the kth node from the end.
    slow = ll.head
    fast = ll.head

    # Step 1: Move 'fast' pointer k steps ahead
    for _ in range(k):
        if fast is None:
            raise IndexError("k is larger than the length of the linked list.")
        fast = fast.next

    # Step 2: Move both 'slow' and 'fast' until 'fast' reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # 'slow' now points to the kth node from the end
    return slow


# Example usage:
if __name__ == "__main__":
    my_list = LinkedList()

    # Append values to the linked list
    for i in [1, 2, 3, 4, 5]:
        my_list.append(i)

    # Retrieve the kth node from the end (k = 5)
    result_node = find_kth_from_end(my_list, 5)

    # Print the entire list
    print(my_list)

    # Print the value of the kth node from the end
    print(f"Kth Node from the end of the linked list: {result_node}")
