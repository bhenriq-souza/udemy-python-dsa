from .types import ListNode


def print_lists(list: ListNode) -> None:
    
    while list:
        print(list.value)
        list = list.next
