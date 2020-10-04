class LinkedList:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f" ->{self.data}"

    def append_node(self, data):
        self.next_node = LinkedList(data)

    def print_linkedlist(self):
        print(self,end="")
        if self.next_node == None:
            return
        else:
            return self.next_node.print_linkedlist()


def main():
    start_node = LinkedList(input("enter the value of start node"))
    no_of_nodes = int(input("enter no of nodes you want"))
    Current_node = start_node
    while no_of_nodes:
        no_of_nodes -= 1
        new_node = input("enter node data")
        Current_node.append_node(new_node)
        Current_node = Current_node.next_node
    flag = int(input("if you want to print data then press 1 or to exit press 0"))
    if flag == 1:
        start_node.print_linkedlist()
    else:
        pass


if __name__ == "__main__":
    main()
