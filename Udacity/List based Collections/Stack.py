# List in python is a stack 
# List Methods - 
# list.append(x)
# list.exted(L)
# list.remove(x)
# list.pop([i])
# list.index(x)
# list.count(x)
# list.sort(cmp=None, key=None. reverse=False)
# list.reverse()

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element

    def insert_first(self, element):
        if self.head:
            current = self.head
            self.head = element
            element.next = current 
        else: 
            self.head = element

    def delete_first(self):
        if self.head:
            current = self.head
            self.head = self.head.next 
            if current: 
                return current       
        else:
            return None

class Stack(object):
    def __init__(self, top = None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
            
    def pop(self):
        return self.ll.delete_first()



e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)
e5 = Element(5)
e6 = Element(6)

stack = Stack(e1)

stack.push(e2)
stack.push(e3)
stack.push(e4)
stack.push(e5)

print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())



