class SinglyLinkedlist:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def addNode(self, data):
        if self.next_node != None:
            self.next_node.addNode(data)
        else:
            self.next_node = SinglyLinkedlist(data)

    def printLinkedList(self):
        print("->", self.data, end=" ")
        if self.next_node != None:
            self.next_node.printLinkedList()

    def printReverse(self):
        if self.next_node != None:
            self.next_node.printReverse()
        print("->", self.data, end=" ")


def main():
    root = SinglyLinkedlist(input("enter root node \n"))
    nodes = list(map(str, input("\nenter nodes separated by space\n").split()))
    for node in nodes:
        root.addNode(node)
    print("\nLinked List\n")
    root.printLinkedList()
    print("\nReverse Linked List\n")
    root.printReverse()


if __name__ == "__main__":
    main()
