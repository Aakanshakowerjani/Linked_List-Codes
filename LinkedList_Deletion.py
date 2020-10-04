class LinkedList:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def add_node(self, data):
        if self.next_node != None:
            self.next_node.add_node(data)
        else:
            self.next_node = LinkedList(data)

    def deletion_fromBegin(self):
        return self.next_node

    def find_length(self, length):
        if self.next_node != None:
            length += 1
            return self.next_node.find_length(length)
        else:
            return length

    def deletion_fromEnd(self):
        length = 0
        length = self.find_length(length)
        current_node = self
        for node in range(length):
            if node == length - 1:
                current_node.next_node = None
            current_node = current_node.next_node

    def deletion_fromPosition(self, position):
        length = 0
        length = self.find_length(length)
        current_node = self
        for node in range(length):
            if node == position - 2:
                current_node.next_node = current_node.next_node.next_node
                break
            current_node = current_node.next_node

    def printNode(self):
        print("->", self.data, end=" ")
        if self.next_node != None:
            self.next_node.printNode()


def main():
    root = LinkedList(int(input("enter root node")))
    nodes = list(map(int, input("enter nodes separated by space").split()))
    for node in nodes:
        root.add_node(node)
    print("\n Initial Linked List")
    root.printNode()
    print("\n After deleting from front")
    root = root.deletion_fromBegin()
    root.printNode()
    print("\n After deleting last node")
    root.deletion_fromEnd()
    root.printNode()
    position = int(input("\n enter position\n"))
    print("\n After deleting from given position")
    root.deletion_fromPosition(position)
    root.printNode()


if __name__ == "__main__":
    main()
