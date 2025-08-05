###########################################################################################################
# Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input,
# and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

# Given this LinkedList:

# 1 -> 2 -> 3 -> 4 -> 5

# If k=1 then return the first node from the end (the last node) which contains the value of 5.

# If k=2 then return the second node from the end which contains the value of 4, etc.

# If the index is out of bounds, the program should return None.

# The find_kth_from_end function should follow these requirements:

# The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

# The fast pointer should move k nodes ahead in the list.

# If the fast pointer becomes None before moving k nodes, the function should return None, as the list is
# shorter than k nodes.

# The slow and fast pointers should then move forward in the list at the same time until the fast pointer
# reaches the end of the list.

# The function should return the slow pointer, which will be at the k-th position from the end of the list.
############################################################################################################
from exercises.linked_list.types import ListNode


def remove_kth_node_from_end(head: ListNode, k: int):
    dummy = ListNode(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for _ in range(k + 1):
        if fast is None:
            return head

        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy.next

def test_remove_kth_node_from_end_single_node():
    head = ListNode(1)
    k = 1
    new_head = remove_kth_node_from_end(head, k)
    assert new_head is None, "Failed on single node list"

def test_remove_kth_node_from_end_multiple_nodes():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    new_head = remove_kth_node_from_end(head, k)
    expected_values = [1, 2, 3, 5]
    current = new_head
    for value in expected_values:
        assert current.value == value, f"Expected {value}, got {current.val}"
        current = current.next
    assert current is None, "List should end here"

test_remove_kth_node_from_end_single_node()

test_remove_kth_node_from_end_multiple_nodes()

print("All test cases passed!")