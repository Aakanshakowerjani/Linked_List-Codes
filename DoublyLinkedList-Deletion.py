class DoublyLinkedList:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node

    def insertAtEnd(self, data):
        if self.next_node != None:
            self.next_node.insertAtEnd(data)
        else:
            self.next_node = DoublyLinkedList(data)
            self.next_node.previous_node = self

    def findLength(self, length):
        if self.next_node != None:
            length += 1
            return self.next_node.findLength(length)
        else:
            return length

    def deletionFromBegin(self):
        self.next_node.previous_node = None
        return self.next_node

    def deletionFromPosition(self, position):
        length = 0
        length = self.findLength(length)
        current_node = self
        for node in range(length):
            if node == position - 1:
                current_node.previous_node.next_node = current_node.next_node
                current_node.next_node.previous_node = current_node.previous_node
                current_node.next_node = None
                current_node.previous_node = None
                break
            else:
                current_node = current_node.next_node

    def deletionFromEnd(self):
        if self.next_node != None:
            self.next_node.deletionFromEnd()
        else:
            self.previous_node.next_node = None
            self.previous_node = None

    def printDoublyLinkedList(self):
        print("->", self.data, end=" ")
        if self.next_node != None:
            self.next_node.printDoublyLinkedList()


def main():
    root = DoublyLinkedList(input("enter root node\n"))
    nodes = list(map(str, input("enter nodes separated by space\n").split()))
    for node in nodes:
        root.insertAtEnd(node)
    print("\nDeletion from Begin\n")
    root = root.deletionFromBegin()
    root.printDoublyLinkedList()

    print("\nDeletion from End\n")
    root.deletionFromEnd()
    root.printDoublyLinkedList()

    pos = int(input("\nenter position\n"))
    print("\nDeletion from given position\n")
    root.deletionFromPosition(pos)
    root.printDoublyLinkedList()


if __name__ == "__main__":
    main()
