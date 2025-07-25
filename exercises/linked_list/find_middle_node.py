#####################################################################
## Find the Middle Node ##
## Implement an algorithm to find the middle term of a Linked List.
##
## Constraints ##
## 1. You can only loop through the linked list once;
## 2. You are not allowed to calculate the length of the linked list;
#####################################################################
from common.node import Node
from linked_list.linked_list import LinkedList


def find_middle_node(linked_list: LinkedList) -> Node:
    slow = linked_list.head
    fast = linked_list.head

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

        if fast and fast.next:
            fast = fast.next

    return slow

def test_find_middle_node_even_elements_list():
    print("1 - Find middle node of list with even number of elements.")

    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    
    result = find_middle_node(linked_list)
    assert result.value == 3, f"Result {result.value} is not correct."

    print(f"Result {result.value} is correct.")

def test_find_middle_node_odd_elements_list():
    print("2 - Find middle node of list with odd number of elements.")
    
    linked_list = LinkedList(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    
    result = find_middle_node(linked_list)
    assert result.value == 3, f"Result {result.value} is not correct."

    print(f"Result {result.value} is correct.")

def test_find_middle_node_single_node_list():
    print("3 - Find middle node of list with one element.")

    linked_list = LinkedList(1)
    result = find_middle_node(linked_list)
    assert result.value == 1, f"Result {result.value} is not correct."

    print(f"Result {result.value} is correct.")


test_find_middle_node_even_elements_list()

test_find_middle_node_odd_elements_list()

test_find_middle_node_single_node_list()
