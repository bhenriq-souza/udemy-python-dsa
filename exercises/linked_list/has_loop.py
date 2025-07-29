####################################################################################################
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached 
# again by continuously following the next pointer. Internally, pos is used to denote the index
# of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1 ##
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#####################################################################################################
from .types import ListNode


def has_loop(head: ListNode) -> bool:
    slow: ListNode = head
    fast: ListNode = head

    while fast.next is not None:
        if slow == fast.next:
            return True
        
        slow = slow.next
        fast = fast.next

        if fast and fast.next:
            fast = fast.next
    
    return False

def test_has_loop_multiple_node_list():
    print("1 - Checking has loop in a list with multiples of elements and no loop.")

    ll = ListNode(0)
    ll.next = ListNode(1)
    ll.next.next = ListNode(2)
    ll.next.next.next = ListNode(3)

    result = has_loop(ll)

    assert not result, f"Result is {result}"

    print(f"Result is {result} correct.")

def test_has_loop_single_node_list():
    print("2 - Checking has loop in a list with one element and no loop.")

    ll = ListNode(0)

    result = has_loop(ll)

    assert not result, f"Result is {result}"

    print(f"Result is {result} correct.")

def test_has_loop_multiple_node_list():
    print("3 - Checking has loop in a list with multiples of elements and a loop.")

    ll = ListNode(0)
    ll.next = ListNode(1)
    ll.next.next = ListNode(2)
    ll.next.next.next = ListNode(3)
    ll.next.next.next.next = ll

    result = has_loop(ll)

    assert result, f"Result is {result}"

    print(f"Result is {result} correct.")

def test_has_loop_single_node_list():
    print("4 - Checking has loop in a list with one element and a loop.")

    ll = ListNode(0)
    ll.next = ll

    result = has_loop(ll)

    assert result, f"Result is {result}"

    print(f"Result is {result} correct.")


test_has_loop_multiple_node_list()

test_has_loop_single_node_list()

test_has_loop_multiple_node_list()

test_has_loop_single_node_list()
