from common.node import Node


class LinkedList:
    def __init__(self, value: any):
        initial_node = Node(value=value)
        self.head: Node = initial_node
        self.tail: Node = initial_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value: any) -> bool:
        new_node = Node(value=value)

        ## in the case of an empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True

        ## in the case of a non-empty list
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return True

    def pop(self) -> Node | None:
        popped_node: Node | None = None

        ## in the case of an empty list
        if self.length == 0:
            return None

        ## in the case of a list with only one node
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node

        ## in the case of a list with more than one node
        temp = self.head
        previous = self.head

        while temp.next is not None:
            previous = temp
            temp = temp.next

        ## here temp.next is None, so temp is the last node
        ## and the previous is the second-to-last node
        popped_node = temp
        self.tail = previous
        self.tail.next = None
        self.length -= 1

        return popped_node
