from Node import * # import Node class

head = "null" # first node of the linked list

class LinkedList():
    def __init__(self):
        self.head = None # set to None for the time being

    # insert after a specific index
    def insert_after_index(self, index, new_node):
        node = self.head # get the first node
        for i in range(index): # loop through by accessing the next node
            node = node.next # move to the next node
            if(i == index-1): # if at the desired index
                new_node.next = node.next # set the next node of the new node to the node currently in its' place
                node.next = new_node # set the next node of the node currently in its' place with the new node

    # remove from a particular index    
    def remove_after_index(self, index):
        print("Removing after index: " + str(index))
        node = self.head
        if(index == 0): # if removing the first node
            self.head = node.next # set head to the next node
        for i in range(index):
            node_before = node # save previous node and current node to connect both
            node = node.next
            if(i == index-1): # when at the desired index
                print("Connecting nodes: " + str(node_before.value) + " and " + str(node.next.value))
                # connect the next node of the previous node with the next node of the current to delete the current node
                node_before.next = node.next 
    
    # travel to a specific index
    def traverse_to_node(self, index):
        print("Traversing to: " + str(index))
        node = self.head # get the first node
        for i in range(index): # stop at index
            node = node.next # move to the next node

    # travel to the end of the linked list
    def traverse_through_linkedlist(self):
        print("Traversing...")
        node = self.head # get the first node
        while node is not None: # while the next node exists
            print(node.value)
            node = node.next # move to the next node