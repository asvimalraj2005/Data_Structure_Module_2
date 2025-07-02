You are given the head of a linked list A and an integer B. Delete the B-th node from the linked list.

Note : Follow 0-based indexing for the node numbering.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        temp=A
        if B==0:
            return A.next
        
        for i in range(B-1):
            temp=temp.next
        temp.next=temp.next.next
    
        return A


