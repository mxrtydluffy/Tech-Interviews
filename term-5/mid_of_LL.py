# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example #1

#_________________________________________________________________________________________________________________________________

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example #2

#_________________________________________________________________________________________________________________________________

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

#                                   Object Notation
#                                         O(n)

def middleNode(head):
    # Initialze slow and fast pointer to head pointer
    slow, fast = head, head
    
    # Continue while fster pointer reaches the last node or goes out of bounds
    # First check if not out of bounds
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # If reach end of the list 
    return slow