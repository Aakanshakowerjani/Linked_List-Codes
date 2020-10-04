class CircularLinkedList:
    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node = self
        self.previous_node = self

    def insertAtBegin(self, data):
        node = CircularLinkedList(data)
        node.previous_node = self.previous_node
        node.next_node = self
        self.previous_node.next_node = node
        self.previous_node = node
        return node

    def insertAtEnd(self, data, root):
        if self.next_node == root:
            node = CircularLinkedList(data)
            self.next_node.previous_node = node
            node.next_node = self.next_node
            self.next_node = node
            node.previous_node = self
        else:
            self.next_node.insertAtEnd(data, root)

    def findLength(self, root, length):
        if self.next_node != root:
            length += 1
            return self.next_node.findLength(root, length)
        else:
            return length

    def insertAtPosition(self, data, pos):
        length = 0
        length = self.findLength(self,length)
        current_node = self
        for node in range(length):
            if node == pos - 1:
                new_node = CircularLinkedList(data)
                new_node.next_node = current_node
                new_node.previous_node = current_node.previous_node
                current_node.previous_node.next_node = new_node
                current_node.previous_node = new_node
            else:
                current_node = current_node.next_node

    def printCircularLL(self, root):
        print("->", self.data, end=" ")
        if self.next_node != root:
            self.next_node.printCircularLL(root)


def main():
    root = CircularLinkedList(input("\nenter root node\n"))
    nodes = list(map(str, input("\nenter nodes separated by space\n").split()))
    for node in nodes:
        root.insertAtEnd(node,root)

    root = root.insertAtBegin(input("\nenter data to insert at begin\n"))
    root.printCircularLL(root)
    root.insertAtEnd(input("\nenter data to insert at end\n"), root)
    root.printCircularLL(root)
    root.insertAtPosition(
        input("\nenter data to insert at pos\n"), int(input("\nenter position\n"))
    )
    root.printCircularLL(root)


if __name__ == "__main__":
    main()
