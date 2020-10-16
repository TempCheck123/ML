class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data
    def next_node(self):
        return self.next


class LinkedList():
    def __init__(self,value=None,next_address=None):
        self.element = value
        self.link = next_address
        self.i = 0
    def add(self,info):
        self.element = info
        new_node = Node(info)
        new_node.next = self.link
        return new_node.next_node()



ds = LinkedList()
ds.add(43)
print(ds.add(43))