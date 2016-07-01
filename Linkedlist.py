class Node(object):

    def __init__(self, data=None, next_node = None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

    def get_value(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class Linkedlist(object):

    def __init__(self,head=None):
        self.head = head

    def __str__(self):
        l = []
        if self.head == None:
            return 'Empty list'
        else:
            current_node = self.head
            while current_node.get_next():
                l.append(str(current_node.get_value()))
                current_node = current_node.get_next()
            l.append(str(current_node.get_value()))
            #import pdb; pdb.set_trace()
            return " ".join(l)


    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.get_next():
                current_node = current_node.get_next()
            current_node.set_next(new_node)

    def delete(self,index):
        current_node = self.head
        while index > 1:
            current_node = current_node.get_next()
            index -= 1
        current_node.set_next(current_node.get_next().get_next())

    def reverse(self):
        current_node = self.head
        prev = Node()
        while current_node:
            next_node = current_node.get_next()
            current_node.set_next(prev)
            prev = current_node
            current_node = next_node
        self.head = prev
        return self

    def search(self,data):
        if self.head == None:
            return None;
        else:
            current_node = self.head
            if current_node.get_value() == data:
                return current_node
            else:
                while current_node.get_next():
                    if current_node.get_value() == data:
                        return current_node
                    current_node = current_node.get_next()

    #def search_all(self, data):
    #    pass

    def insert(self,index,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.get_next() and index > 1:
            current_node = current_node.get_next()
            index -= 1
        new_node.set_next(current_node.get_next())
        current_node.set_next(new_node)


    def size(self):
        index = 0
        if self.head == None:
            return 0
        else:
            current_node = self.head
            while current_node.get_next():
                index += 1
                current_node = current_node.get_next()
            return index


l_list = Linkedlist()
for i in range(100):
    l_list.add(i)
l_list.insert(2,1000)
print(l_list)
l_list.delete(2)
print(l_list)
print("size of the linkedlist: {}".format(l_list.size()))
print("element search result: {}".format(l_list.search(1000)))
print(l_list.reverse())
