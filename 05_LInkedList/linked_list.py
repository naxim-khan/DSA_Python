class Node:
    """An object for storing a single node of a linked list. Models two attributes - data and the link to the next node in the list """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "Node data: %s" % self.data
    

# N1 = Node(10)
# print('N1 = ',N1)

# N2 = Node(20)
# N1.next_node = N2
# print('n1 next node: ', N1.next_node)

class LinkedList:

    def __init__(self):
        self.head = None

    def is_emtpy(self):
        return self.head == None
    
    def size(self):
        '''Return the numbers of nodes in the list takes O(n) time'''
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count