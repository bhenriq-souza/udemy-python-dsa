####################################################################################################
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle,
# return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by 
# continuously following the next pointer. Internally, pos is used to denote the index of the node 
# that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos 
# is not passed as a parameter.

# Do not modify the linked list.
####################################################################################################
from exercises.linked_list.types import ListNode


def has_loop(head: ListNode):
    visited = set()
    current = head
    position = -1

    while current and current.next:
        position += 1
        
        if current in visited:
            return current

        visited.add(current)
        current = current.next

    return None

def test_has_loop_single_node_list_no_loop():
    print("1 - Checking has loop in a single node list with no loop.")

    ll = ListNode(1)
    result = has_loop(ll)
    
    assert result is None, f"Expected None, got {result}"
    
    print(f"Result is {result} correct.")

def test_has_loop_multiple_node_list_no_loop():
    print("2 - Checking has loop in a multiple node list with no loop.")

    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    result = has_loop(ll)
    
    assert result is None, f"Expected None, got {result}"
    
    print(f"Result is {result} correct.")

def test_has_loop_multiple_node_list_with_loop():
    print("3 - Checking has loop in a multiple node list with a loop.")

    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ll

    result = has_loop(ll)

    assert result.value == ll.value, f"Expected {ll}, got {result}"
    
    print(f"Result is {result.value} correct.")
    

test_has_loop_single_node_list_no_loop()
test_has_loop_multiple_node_list_no_loop()
test_has_loop_multiple_node_list_with_loop()
