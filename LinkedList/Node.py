value = 0 # value of the node
next = "null" # next node to this one

class Node():
    def __init__(self, val):
        self.value = val
        self.next = None
        print("New Node Created: " + str(val))
