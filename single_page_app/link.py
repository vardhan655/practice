# #create
# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# head = node(10)
# second = node(20)
# third = node(30)
# head.next = second
# second.next = third
# print(head.data)
# print(head.next.data)
# print(third.data)
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head
        while current is not None:
            print(current.data,end = "->")
            current = current.next
        print("none")
#insert at first
    def firstadd(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
#insert at last
    def lastadd(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
#insert at a position
    def position(self,index,data):
        if index<0:
            raise IndexError("invalid")
        if index == 0:
            self.firstadd(data)
            return 
        current = self.head
        for _ in range(index-1):
            if current is None:
                raise IndexError("out of range")
            current = current.next
        if current is None:
            raise IndexError("out of range")
        new_node = node(data)
        new_node.next = current.next
        current.next = new_node
#insert after the fisrt occurence
    def first_occurence(self,target,data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = node(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        return False
#delete from beginning
    def delete_begin(self):
            if self.head is None:
                return None
            removed_value = self.head.data
            self.head = self.head.next
            return removed_value
#delete the end 
    def delete_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed = self.head.data
            self.head = None
            return removed
        current = self.head
        while current.next.next is not None:
            current = current.next
        removed = current.next.data
        current.next  = None
        return removed
#delete the first occurence
    def first_occurence(self,target):
        if self.head is None:
            return None
        if self.head == target:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == target:
                current.next = current.next.next
                return True
            current = current.next
        return False
#delete at index
    def delete_index(self,index):
        if index<0 or self.head is None:
            raise IndexError("invalid")
        if index == 0:
            return self.delete_begin()
        current = self.head
        for _ in range(index-1):
            if current.next is None:
                raise IndexError("invalid")
            current = current.next
        if current.next is None:
            raise IndexError("invalid")
        remove = current.next.data
        current.next = current.next.next
        return remove
#search an element
    def search(self,target):
        current = self.head
        index = 0
        while current is not None:
            if current.data == target:
                return index
            current = current.next
            index+=1
        return -1
#node value by index
    def node_value(self,index):
        if index<0:
            raise IndexError("invalid")
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("invalid")
            current = current.next
        if current is None:
            raise IndexError("invalid")
        return current.data
        

l1 = linkedlist()
l1.head = node(10)
l1.head.next = node(20)
l1.head.next.next = node(30)
l1.firstadd(40)
l1.firstadd(50)
l1.lastadd(70)
l1.lastadd(80)
l1.position(2,55)
l1.display()
