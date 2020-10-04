class DoublyLL:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node

    def insert_atEnd(self, data):
        if self.next_node != None:
            self.next_node.insert_atEnd(data)
        else:
            self.next_node = DoublyLL(data)
            self.next_node.previous_node = self

    def insert_atBegin(self, data):
        root = DoublyLL(data)
        root.next_node = self
        self.previous_node = root
        return root

    def findLength(self, length):
        if self.next_node != None:
            length += 1
            return self.next_node.findLength(length)
        else:
            return length

    def insert_atPosition(self, data, position):
        length = 0
        length = self.findLength(length)
        current_node = self
        for node in range(length):
            if node == position - 1:
                new_node = DoublyLL(data)
                new_node.next_node = current_node
                new_node.previous_node = current_node.previous_node
                current_node.previous_node.next_node = new_node
                current_node.previous_node = new_node
                break
            else:
                current_node = current_node.next_node

    def printDoublyLL(self):
        print('->',self.data,end=" ")
        if self.next_node != None:
            self.next_node.printDoublyLL()


def main():
    root = DoublyLL(input("enter root node"))
    nodes = input("enter nodes separated by space").split()
    for node in nodes:
        root.insert_atEnd(node)

    node = input("\nInsert at Begin\n enter node \n")
    root = root.insert_atBegin(node)
    root.printDoublyLL()

    node = input("\nInsert at Position\n enter node \n")
    pos = int(input("enter position"))
    root.insert_atPosition(node, pos)
    root.printDoublyLL()

    node = input("\nInsert at End\n enter node \n")
    root.insert_atEnd(node)
    root.printDoublyLL()


if __name__ == "__main__":
    main()
