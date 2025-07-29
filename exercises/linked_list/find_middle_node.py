#####################################################################
## Find the Middle Node ##
## Implement an algorithm to find the middle term of a Linked List.
##
## Constraints ##
## 1. You can only loop through the linked list once;
## 2. You are not allowed to calculate the length of the linked list;
#####################################################################
from .types import ListNode


def find_middle_node(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

        if fast and fast.next:
            fast = fast.next
 
    return slow

def test_find_middle_node_even_elements_list():
    print("1 - Find middle node of list with even number of elements.")

    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)
    linked_list.next.next.next = ListNode(4)
    
    result = find_middle_node(linked_list)
    assert result.value == 3, f"Result {result.value} is not correct."

    print(f"Result {result.value} is correct.")

def test_find_middle_node_odd_elements_list():
    print("2 - Find middle node of list with odd number of elements.")
    
    linked_list = ListNode(1)
    linked_list.next = ListNode(2)
    linked_list.next.next = ListNode(3)
    linked_list.next.next.next = ListNode(4)
    linked_list.next.next.next.next = ListNode(5)
    linked_list.next.next.next.next.next = ListNode(6)
    linked_list.next.next.next.next.next.next = ListNode(7)
    
    result = find_middle_node(linked_list)
    assert result.value == 4, f"Result {result.value} is not correct."

    print(f"Result {result.value} is correct.")

def test_find_middle_node_single_node_list():
    print("3 - Find middle node of list with one element.")

    linked_list = ListNode(1)
    result = find_middle_node(linked_list)
    assert result.value == 1, f"Result {result.value} is not correct."

    print(f"Result {result.value} is correct.")


test_find_middle_node_even_elements_list()

test_find_middle_node_odd_elements_list()

test_find_middle_node_single_node_list()
