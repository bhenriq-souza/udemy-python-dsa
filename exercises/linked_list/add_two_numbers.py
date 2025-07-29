#############################################################################################
## Add Two Numbers ##
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Example 1 ##
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

## Example 2 ##
# Input: l1 = [0], l2 = [0]
# Output: [0]

## Example 3 ##
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# ll = [<unidade>, <dezena>, <centena>]
#############################################################################################
from .types import ListNode
from .helpers import print_lists


def add_two_numbers(l1, l2):
    head = ListNode()
    current = head
    carry = 0

    while l1 or l2 or carry:
        value1 = l1.value if l1 else 0
        value2 = l2.value if l2 else 0

        sum = value1 + value2 + carry
        carry = sum // 10
        digit = sum % 10
        
        current.next = ListNode(digit)
        current = current.next

        if l1:
            l1 = l1.next
        
        if l2:
            l2 = l2.next
    
    return head.next

l1 = ListNode(2)
l1.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

result = add_two_numbers(l1, l2)
print_lists(result)
