class CircularLinkedList:
    def __init__(self, data, next_node=None, previous_node=None):
        self.data = data
        self.next_node = self
        self.previous_node = self

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

    def deletionFromBegin(self):
        self.previous_node.next_node = self.next_node
        self.next_node.previous_node = self.previous_node
        return self.next_node

    def deletionFromEnd(self, root):
        if self.next_node == root:
            self.previous_node.next_node = self.next_node
            self.next_node.previous_node = self.previous_node
            self.next_node = None
            self.previous_node = None
        else:
            self.next_node.deletionFromEnd(root)

    def deletionFromPosition(self, position):
        length = 0
        length = self.findLength(self, length)
        current_node = self
        for node in range(length):
            if node == position - 1:
                current_node.previous_node.next_node = current_node.next_node
                current_node.next_node.previous_node = current_node.previous_node
                current_node.next_node = None
                current_node.previous_node = None
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
        root.insertAtEnd(node, root)
    print('Circular Linked List')
    root.printCircularLL(root)

    root = root.deletionFromBegin()
    print('\nDeletion From begin\n')
    root.printCircularLL(root)
    root.deletionFromEnd(root)
    print('\nDeletion From End\n')
    root.printCircularLL(root)
    root.deletionFromPosition(int(input("\nenter position\n")))
    print('\nDeletion From Position\n')
    root.printCircularLL(root)


if __name__ == "__main__":
    main()
