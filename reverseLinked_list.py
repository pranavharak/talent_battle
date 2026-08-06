class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class list:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        curr = self.root
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.root = prev


    def display(self):
        if self.root is None:
            print("empty ")
            return
        temp = self.root
        while temp is not None:
            print(f"{temp.val}->",end="")
            temp = temp.next
        print("None")

obj = list()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.display() 
obj.reverse()
obj.display()      