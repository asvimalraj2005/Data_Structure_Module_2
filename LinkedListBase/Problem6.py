You are given a singly linked list having head node A. You have to inverse the linked list and return the head node of that inversed list.

NOTE: You have to do it in-place and in one-pass.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def inverseList(self, A):
        curr = A
        prev = None

    # Traverse all the nodes of Linked List
        while curr is not None:

        # Store next
            nextNode = curr.next

        # Reverse current node's next pointer
            curr.next = prev

        # Move pointers one position ahead
            prev = curr
            curr = nextNode

    # Return the head of reversed linked list
        return prev


