class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            #print ("EL:",node,"VAL:",node.value,"NEXT:",node.next)
            node = node.next
            
        #print ("HEAD:",self.head,"TAIL:",self.tail)
        #print ("LEN:",self.len())

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        arr = [];
        node = self.head
        while node != None:
            if node.value == val:
                arr.append(node)
            node = node.next
        if len(arr) > 0:
            return arr
        return arr
        
    def delete(self, val, all=False):
        node = self.head
        prev = self.head
        count = 0
        while node != None:
            #print ("Working on", node, "PREV:",prev, "NEXT:",node.next)            
            if node.value == val:
                #print ("DELETING...")
                if node == self.head and node == self.tail:
                    self.head = None
                    self.tail = None
                    return
                elif node == self.head:
                    self.head = node.next
                elif node == self.tail:
                    self.tail = prev
                prev.next = node.next
                count += 1
                if (all == False):
                    return count
            else:
                prev = node    
            node = node.next
            self.print_all_nodes()
            #print ("------------------")
        return count 
        
    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head
        while node != None:
            count = count + 1
            node = node.next
        return count
        
    def insert(self, afterNode, newNode):
        if self.len() == 0 and afterNode == None:
            self.add_in_tail(newNode)
            return True
        #if afterNode == None: 
        #    newNode.next = self.head
        #    self.head = newNode
        #    return True
        newNode.next = afterNode.next
        afterNode.next = newNode
        if afterNode == self.tail:
            self.tail = newNode
        return True
