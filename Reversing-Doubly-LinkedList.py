class DoubleLinkedList:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node

    def add_node(self, data):
        if self.next_node != None:
            self.next_node.add_node(data)
        else:
            node = DoubleLinkedList(data)
            node.previous_node=self
            self.next_node = node

    def printLinkedList(self):
        print("->", self.data, end=" ")
        if self.next_node != None:
            self.next_node.printLinkedList()

    def lastNode(self):
        if self.next_node != None:
            return self.next_node.lastNode()
        else:
            return self

    def printReverse(self):
        print("->", self.data, end=" ")
        if self.previous_node != None:
            self.previous_node.printReverse()


def main():
    root = DoubleLinkedList(input("\nenter the root node\n"))
    nodes = list(map(str, input("\nenter nodes separated by space\n").split()))
    for node in nodes:
        root.add_node(node)
    print("\nDouble Linked List\n")
    root.printLinkedList()
    last_node = root.lastNode()
    print("\nReverse of Linked List\n")
    last_node.printReverse()


if __name__ == "__main__":
    main()
