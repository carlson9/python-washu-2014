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
        holder = [] #rather than call hasCycle function, do the cycle - decreases complexity of computation - would still be linear, but twice as many computations
        hold = self.head
        count = 0
        while hold is not None: #loop until pointer is none
            if hold in holder: #if it cycles, break count
                print 'List is cyclical: length is length until fold.'
                return count + 1
            holder.append(hold) #couldn't figure out how to do this without a list - without cycles don't need the list
            hold = hold.next #move down one
            count+=1
        return count

    def addNode(self, new_value):
        node = Node(new_value) #create node and send it to addNodeAsNode function
        self.addNodeAsNode(node)

    def addNodeAsNode(self, node): #need this to create cycles and helps the reversal function
        if self.hasCycle(): #could have done this within the function again to decrease complexity, but it also increases code length
            print 'Cannot add node to cyclical list: use addNodeBefore or addNodeAfter'
            return None
        hold = self.head
        while hold.next is not None: hold = hold.next #O(n) complexity
        hold.next = node #add node once pointer is none

    def addNodeAfter(self, new_value, after_node):
        hold = self.head
        while hold is not after_node: #loop until pointing at after node
            if hold is None: #got to end
                print 'There was no node matching argument.'
                return None
            hold = hold.next #O(n) complexity
        hold.next = Node(new_value, hold.next) #insert it by pointing before node to new node and new node points to after node


    def addNodeBefore(self, new_value, before_node):
        node = Node(new_value) #same logic as addNode
        self.addNodeBeforeAsNode(node, before_node)

    def addNodeBeforeAsNode(self, node, before_node): #helps with reversal function
        node.next=before_node #point to before node
        hold = self.head
        if hold is before_node: #if before node is first node, make head new node
            self.head = node
        else:
            while hold.next is not before_node: #loop until reach penultimate node - O(n) complexity
                if hold.next is None: #if reached end
                    print 'There is no node matching argument.'
                    return None
                hold = hold.next
            hold.next = node

    def removeNode(self, node_to_remove):
        hold = self.head
        if hold is None:
            print 'This is an empty list with no nodes to remove.'
            return None
        if hold is node_to_remove: #if head is node to remove
            self.head = hold.next
            return None
        while hold.next is not node_to_remove: #loop until find node - O(n) complexity
            if hold.next is None: #if reached end
                print 'There is no node matching argument.'
                return None
            hold = hold.next
        hold.next = hold.next.next #simply point before node to after node

    def removeNodesByValue(self, value):
        hold = self.head
        if hold.value == value:
            self.removeNode(hold) #remove head node if equals value - easier to remove head if value than to try to include head in loop
            if self.head is not None: return self.removeNodesByValue(value) #if not at end, recursively call function with new head
            else: return None
        while hold.next is not None: #could use length function but would add complexity
            if hold.next.value == value:
                hold.next = hold.next.next
            hold = hold.next
            if hold is None: break #if removed last node need to break the loop or the hold.next in the while check would error

    def reverse(self):
        if self.hasCycle(): #doesn't make sense to reverse a cyclical list. if the list is a->b->c->b there is no natural breaking point to turn
            print 'List is cyclical. Cannot reverse.'
            return None
        hold1 = self.head #hold the head
        self.removeNode(self.head) #remove the head
        hold1.next = None #make the holder point to None - will be last in list
        self.addNodeAsNode(hold1) #add holder to end
        for i in range(self.length()-2): #O(n) - length has to loop through til end as well as this loop, so it's 2n complexity, but still linear
            hold2 = self.head #hold the head
            self.removeNode(self.head) #remove the head
            self.addNodeBeforeAsNode(hold2, hold1) #add it back in behind the last one put in
            hold1 = hold2 #last one put in becomes the next point

    def hasCycle(self): #determines if the list cycles back onto it itself
        holder = [] #store the nodes in a list - couldn't figure out how to do this without a list
        hold = self.head #store head
        while hold is not None: #loop until end
            if hold in holder: return True #if the hold is in the list already, break the loop and return True
            holder.append(hold) #append the node to the 
            hold = hold.next
        return False

    def __str__(self):
        output = ""
        holder = []
        hold = self.head
        while hold is not None:
            if hold in holder:
                print 'This is a cyclical list. Printing until it folds.'
                return output + str(hold)
            holder.append(hold)
            output += str(hold) + ', '
            hold=hold.next
        return output[:-2]

#for some functions, could have called hasCycle to see if some processes were necessary, but it would be looping through in the function and if looping through anyways might as well have it in the function. E.g. str function could run hasCycle instead of checking for cycle within function, but it would double the necessary looping. It would still have a linear complexity, but twice as much computation. I had to use lists to deal with cycles, and I couldn't figure out how to have cycles without using a list. The actual LinkedList does not use any lists.

