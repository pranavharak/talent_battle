class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class list():
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
    def display(self):
        if self.root is None:
            print("list is empty")
            return
        temp = self.root
        
        while temp is not None:
            print(f"{temp.data}->",end="")
            temp = temp.next
        print("None")
    
    def delete(self):
        cnt = 0
        temp = self.root
        while temp is not None:
            cnt+=1
            temp =temp.next

        if cnt<2:
            return
        
        res = cnt - 3
        if res < 0:
            self.root = self.root.next
            return

        temp = self.root
        i = 0
        while i < res:
            temp = temp.next
            i+=1

        temp.next = temp.next.next

obj = list()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.display()
obj.delete()
obj.display()