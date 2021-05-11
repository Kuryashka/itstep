class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f"Node data {self.data}"
# HEAD | Node("b") -> Node(24) -> Node("st") -> None

class LinkedList:
    
    def __init__(self, nodes) -> None:
        self.head = None
        if nodes is not None:
            current_node = Node(nodes.pop(0))
            self.head = current_node
            for elem in nodes:
                current_node.next = Node(elem)
                current_node = current_node.next
            
    def length(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return f'the amount of nodes is: {count}'

    def insert(self, data, position):
        ''' insert a node at a specific position if the position is none - insert a node to the end of the list '''
        node = Node(data)
        if self.head is not None:
            self.head = node
        else:
            temp = self.head
            count = 1
            while temp is not None and count < position:
                temp = temp.next
                count += 1
                node.next = temp.next
                temp.next = node
        return self.head   

    def find(self, searched_data):
        node = self.head
        while node is not None:
            if node.data == searched_data:
                return node
            node = node.next
        return None

    def remove(self, data):
        '''
        Remove first element with data and return True if success else return False
        '''
        previous_node = None
        node = self.head
        while node is not None:
            if node.data == data:
                if previous_node is None:
                    self.head = node.next
                    del node
                    return True
                previous_node.next = node.next
                del node
                return True
            previous_node = node
            node = node.next
        return False

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == "__main__":
    linked_list = LinkedList(['b', "24", "st", "1213"])


    print(linked_list)

    print(linked_list.remove("b"))
    print(linked_list.remove("1213"))
    print(linked_list.length())
    print(linked_list.insert('3', 2))
    print(linked_list)
    print(linked_list.length())

    
