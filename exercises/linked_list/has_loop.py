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
