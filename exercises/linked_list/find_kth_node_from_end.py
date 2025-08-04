from exercises.linked_list.types import ListNode


def find_kth_from_end(head: ListNode, k: int) -> ListNode | None:
    fast = head
    slow = head

    for _ in range(k):
        if fast is None:
            return None
        
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow
        

def test_find_kth_from_end_single_node():
    head = ListNode(1)
    assert find_kth_from_end(head, 1) == head
    assert find_kth_from_end(head, 2) is None

def test_find_kth_from_end_multiple_nodes():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert find_kth_from_end(head, 1) == head.next.next.next.next
    assert find_kth_from_end(head, 2) == head.next.next.next
    assert find_kth_from_end(head, 3) == head.next.next
    assert find_kth_from_end(head, 4) == head.next
    assert find_kth_from_end(head, 5) == head
    assert find_kth_from_end(head, 6) is None

def test_find_kth_from_end_empty_list():
    head = None
    assert find_kth_from_end(head, 1) is None
    assert find_kth_from_end(head, 0) is None
    assert find_kth_from_end(head, -1) is None

def test_find_kth_from_end_invalid_k():
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert find_kth_from_end(head, 0) is None
    assert find_kth_from_end(head, -1) is None
    assert find_kth_from_end(head, 4) is None
    assert find_kth_from_end(head, 100) is None    

test_find_kth_from_end_single_node()
test_find_kth_from_end_multiple_nodes()
test_find_kth_from_end_empty_list()
test_find_kth_from_end_invalid_k()
print("All tests passed.")