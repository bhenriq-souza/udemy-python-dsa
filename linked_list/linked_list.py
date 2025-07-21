from common.node import Node


class LinkedList:
    def __init__(self, value: any):
        """ Initializes a new linked list with a single 
            node containing the given value.
        """
        initial_node = Node(value=value)
        self.head: Node = initial_node
        self.tail: Node = initial_node
        self.length = 1
    
    def empty_list(self) -> None:
        """ Resets the linked list to an empty state. \n
            Complexity: O(1)
        """
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self) -> None:
        """ Prints the values of the linked list nodes. \n
            Complexity: O(n), where n is the number of nodes in the list. \n
            This is because we traverse the entire list to print each node's value.
        """
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Complexity of O(1)
    def append(self, value: any) -> bool:
        """ Appends a new node with the given value to the end of the linked list. \n
            Complexity: O(1) \n
            Parameters:
                value (any): The value to be stored in the new node.
            Returns:
                bool: True if the operation is successful.
        """
        new_node = Node(value=value)

        # in the case of an empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return True

        # in the case of a non-empty list
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return True

    # Complexity of O(n)
    def pop(self) -> Node | None:
        """ Removes the last node from the linked list and returns it. \n
            Complexity: O(n)
            Returns:
                Node | None: The popped node or None if the list is empty.
        """
        popped_node: Node | None = None

        # in the case of an empty list
        if self.length == 0:
            return None

        # in the case of a list with only one node
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped_node

        # in the case of a list with more than one node
        temp = self.head
        previous = self.head

        while temp.next is not None:
            previous = temp
            temp = temp.next

        # here temp.next is None, so temp is the last node
        # and the previous is the second-to-last node
        popped_node = temp
        self.tail = previous
        self.tail.next = None
        self.length -= 1

        return popped_node
    
    # Complexity of O(1)
    def prepend(self, value: any) -> bool:
        """ Prepends a new node with the given value to the start of the linked list. \n
            Complexity: O(1)
            Parameters:
                value (any): The value to be stored in the new node.
            Returns:
                bool: True if the operation is successful.
        """
        new_node = Node(value=value)
        
        # in the case of an empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1

            return True
        
        past_head = self.head
        self.head = new_node
        self.head.next = past_head
        self.length += 1

        return True
