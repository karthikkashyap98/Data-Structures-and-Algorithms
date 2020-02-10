class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head 
        if self.head:
            while current.next:
                current = current.next 
            current.next = new_element    
        else:
            self.head = current 

    def get_position(self, position):
        count = 1
        current = self.head
        if self.head:
            if position == 1:
                return current.value
            while current.next:
                current = current.next 
                count += 1 
                if count == position:
                    return current.value
        else:
            return None       

    def insert(self, new_element, position):
        if self.head:
            current = self.head
            count = 1
            while current.next:
                if count == position - 1:
                    new_element.next = current.next 
                    current.next = new_element
                    return 
                current = current.next 
                count += 1
        else:
            self.head = new_element

    def delete(self, value):
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
            current = self.head
            while current:
                if current.next == None:
                    return 
                if current.next.value == value:
                    current.next = current.next.next 
                    return 
                current = current.next      
                    
                            
                               


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)
e7 = Element(7)

l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)
l1.append(e4)
l1.append(e5)
l1.append(e7)

print(l1.head.next.next.value)
print(l1.get_position(6))

l1.insert(e6, 6)
print(l1.get_position(6))


l1.delete(2)
print(l1.get_position(2))