from Node import *
from LinkedList import *

# create a linked list
ll = LinkedList()

# set the head as the new node created with the value 5
ll.head = Node(5)

second_node = Node(6)

# set the next of the head to our second node
ll.head.next = second_node

third_node = Node(7)
second_node.next = third_node

# print the entire list
ll.traverse_through_linkedlist()

ll.insert_after_index(1, Node(8))

ll.traverse_through_linkedlist()

# remove the second node
ll.remove_after_index(1)

ll.traverse_through_linkedlist()