"""
Given only a reference to a specific node in a linked list, delete that node from a singly-linked list.

Example:

The code below should first construct a linked list (x -> y -> z) and then delete `y` from the linked list by calling the function `delete_node`. It is your job to write the `delete_node` function.

```python
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(y)
```

*Note: We can do this in O(1) time and space! But be aware that our solution will have some side effects...*
"""
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None
# This should be impossible??
# How do you walk backwards in a single linked list?
# If all you're given, is the node to delete..
# How you walk backwards?
#def delete_node(node_to_delete):
    # Your code here
# And so he changes the code....    


def delete_node(head, index):
    current = head
    while current and index > 2:
        #2 because linked lists 'start' at 1, and we stop at the node before
        index -= 1
        current = current.next
    current.next = current.next.next

def delete_node_instructor(head, index):
    current = head
    counter = 1
    while cunter != index - 1:
        current = current.next
        counter += 1
    current.next = current.next.next     

def print_ll(current):
    while current is not None:
        print(current.value)
        current = current.next

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

delete_node(x, 2)
print_ll(x)
