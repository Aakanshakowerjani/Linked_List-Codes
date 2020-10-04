class LinkedList:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return f"-> {str(self.data)}"

    def get_last_node(self):
        if self.next_node == None:  # This conditions checks if this is the last node
            return self
        else:
            return self.next_node.get_last_node()

    def get_first_occurance(self, data):
        if self.data == data:
            return self
        else:
            return self.next_node.get_first_occurance(data)

    def replace_first_occurance(self, old_data, new_data):
        old_node = self.get_first_occurance(old_data)
        old_node.data = new_data

    def get_preceeder_of_first_occurance(self, data):
        if self.next_node == None:
            return None
        if self.next_node.data == data:
            return self
        else:
            return self.next_node.get_preceeder_of_first_occurance(data)

    def delete_first_occurance(self, data):
        preceeder_node = self.get_preceeder_of_first_occurance(data)
        if preceeder_node != None:
            preceeder_node.next_node = preceeder_node.next_node.next_node

    def get_node_by_index(self, index):
        if index == 0:
            return self
        else:
            counter = 0
            current_node = self.next_node
            while current_node != None:
                counter += 1
                if counter == index:
                    return current_node
                current_node = current_node.next_node

    def append_middle_node(self,index,data):
        if index == 0:
            new_node=LinkedList(data)
            new_node.next_node = self
        else:
            current_node=self.get_node_by_index(index)
            next_of_current_node=current_node.next_node
            current_node.next_node=LinkedList(data)
            current_node.next_node.next_node=next_of_current_node


    def append_node(self, data):
        last_node = self.get_last_node()
        last_node.next_node = LinkedList(data)

    def print_linkedlist(self):
        print(self, end=" ")
        if self.next_node == None:
            print()
            return
        self.next_node.print_linkedlist()
        
    def print_reverse(self):
        if self.next_node == None:  # This conditions checks if this is the last node
            print(self,end=" ")
            return
        
        self.next_node.print_reverse()
        print(self,end=" ")
        



def main():
    my_li = LinkedList(1)
    numbers = [2, 3, 5, 6, 7, 8, 7]
    for number in numbers:
        my_li.append_node(number)
    my_li.print_linkedlist()
    # my_li.replace_first_occurance(7, 0)
    # my_li.print_linkedlist()
    # my_li.replace_first_occurance(5,0)
    # my_li.print_linkedlist()
    # my_li.delete_first_occurance(7)
    # my_li.print_linkedlist()
    # my_li.delete_first_occurance(7)
    # my_li.print_linkedlist()
    # my_li.delete_first_occurance(2)
    # my_li.print_linkedlist()

    # indexed_node = my_li.get_node_by_index(5)
    # print(indexed_node)
    # indexed_node = my_li.get_node_by_index(0)
    # print(indexed_node)
    # indexed_node = my_li.get_node_by_index(7)
    # print(indexed_node)
    # my_li.append_middle_node(5,9)
    # my_li.print_linkedlist()
    # my_li.append_middle_node(0,9)
    # my_li.print_linkedlist()
    my_li.print_reverse()

if __name__ == "__main__":
    main()
