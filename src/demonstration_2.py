"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head):
    current = head
    previous = None
    while current:
        # tried to use 'next' apparantly it's a keyword!
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous #Return the last/first node


def reverse_instructor(head_of_list):
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node

    return previous_node

head = LinkedListNode('A')
current = head
for i in range(25):
    current.next = LinkedListNode(chr(66 + i))
    current = current.next

def print_ll(current):
    while current is not None:
        print(current.value)
        current = current.next

print_ll(head)
print("And now reverse!")
print_ll(reverse(head))
