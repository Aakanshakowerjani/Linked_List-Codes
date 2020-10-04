class LinkedList:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def add_node_inlast(self, data):
        if self.next_node != None:
            self.next_node.add_node_inlast(data)
        else:
            self.next_node = LinkedList(data)

    def add_node_inbegin(self, data):
        root = LinkedList(data)
        root.next_node = self
        return root

    def find_length(self, length):
        if self.next_node != None:
            length += 1
            return self.next_node.find_length(length)
        return length

    def add_node_inPosition(self, data, position):
        length = 0
        length = self.find_length(length)
        current_node = self
        for node in range(length):
            if node == position - 2:
                new_node = LinkedList(data, current_node.next_node)
                current_node.next_node = new_node
            else:
                current_node = current_node.next_node

    def printLinkedList(self):
        print("->", self.data, end=" ")
        if self.next_node != None:
            self.next_node.printLinkedList()


def main():
    root = LinkedList(int(input("enter root node")))
    nodes = list(map(int, input("enter nodes").split()))
    for node in nodes:
        root.add_node_inlast(node)

    print("Initial Linked List")
    root.printLinkedList()

    while True:
        input1 = int(
            input(
                "\n select one option\n 1. Insert in begining \n 2. Insert in End \n 3. Insert in given position \n 4. Printing Linked List \n 5. Exit \n"
            )
        )
        if input1 == 1:
            node = int(input("enter node data"))
            root = root.add_node_inbegin(node)

        elif input1 == 2:
            node = int(input("enter node data"))
            root.add_node_inlast(node)

        elif input1 == 3:
            node = int(input("enter node data"))
            position = int(input("enter position"))
            root.add_node_inPosition(node, position)

        elif input1 == 4:
            root.printLinkedList()

        else:
            break


if __name__ == "__main__":
    main()
