class Node:
    def __init__(self, _value=None, _next=None):
        self.value = int(_value)
        self.next = _next
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def length(self):
        count = 1
        hold = self.head
        while hold.next is not None: #O(n) complexity
            count+=1
            hold = hold.next
        return count

    def addNode(self, new_value):
        hold = self.head
        while hold.next is not None: hold = hold.next #O(n) complexity
        hold.next = Node(new_value)

    def addNodeAfter(self, new_value, after_node):
        hold = self.head
        while hold is not after_node: hold = hold.next #O(n) complexity
        hold.next = Node(new_value, hold.next)

    def addNodeBefore(self, new_value, before_node):
        hold = self.head
        if hold is before_node:
            self.head = Node(new_value, before_node)
        else:
            while hold.next is not before_node: hold = hold.next #O(n) complexity
            hold.next = Node(new_value, before_node)

    def removeNode(self, node_to_remove):
        hold = self.head
        if hold is node_to_remove:
            self.head = hold.next
            return None
        while hold.next is not node_to_remove: hold = hold.next #0(n) complexity
        hold.next = hold.next.next

    def removeNodesByValue(self, value):
        hold = self.head
        if hold.value == value:
            self.removeNode(hold)
            if self.head is not None: return self.removeNodesByValue(value)
            else: return None
        while hold.next is not None: #could use length function but would add a degree of complexity
            if hold.next.value == value:
                hold.next = hold.next.next
            hold = hold.next
            if hold is None: break

    def reverse(self):
        self.addNode(self.head.value)
        hold = self.head
        self.removeNode(self.head)
        for i in range(self.length()-2): #O(n^2) add has to loop through til end as well as this loop
            self.addNodeBefore(self.head.value, hold)
            hold = self.head
            self.removeNode(self.head)

    def __str__(self):
        hold = self.head
        output = '['
        while hold.next is not None:
            output += str(hold)+', '
            hold=hold.next
        output += str(hold) + ']'
        return output

        
        



