class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f"Node data {self.data}"
# HEAD | Node("b") -> Node(24) -> Node("st") -> None

class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.c = 0

    def __repr__(self):
        string = ''

        if self.head == None:
            string += "The list is empty"
            return string

        string += f"Doubly Linked List:\n{self.head.data}"
        start = self.head.next

        while start != None:
            string += f" -> {start.data}"
            start = start.next
        return string

    #appending a node if the list is empty
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.c += 1
            return

        self.tail.next = Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next
        self.c += 1

    def insert(self, data, index):
        if index > self.c or index < 0:
            raise ValueError("index is out of range")

        if index == self.c:
            self.append(data)
            return

        if index == None:
            self.append(data)
            return

        start = self.head
        for i in range(index):
            start = start.next
        start.prev.next = Node(data)
        start.prev.next.prev = start.prev
        start.prev.next.next = start
        start.prev = start.prev.next
        self.c += 1
        return
    
    def remove(self, index):
        if index > self.c or index < 0:
            raise ValueError("index is out of range")
        
        if index == None:
            self.tail = self.tail.prev
            self.tail.next = None
            self.c -= 1
            return
        
        start = self.head
        for i in range(index):
            start = start.next
        start.prev.next = start.next
        start.next.prev = start.prev
        self.c -= 1
        return
    
    def length(self):
        return self.c

    def show(self):
        print(self)



    


if __name__ == "__main__":

    l = DoublyLinkedList()
    l.append(1)
    l.append(12)
    l.append('k')
    l.show()
    l.insert('j', 1)
    l.show()
    l.remove(1)
    l.show()
    print(l.length())
