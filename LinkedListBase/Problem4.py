Given a linked list A, remove the B-th node from the end of the list and return its head.
For example, given linked list: 1->2->3->4->5, and B = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.

Try doing it using constant additional space.

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
        temp=A
        
            

        count=0
        
        while temp is not None:
            count=count+1
            temp=temp.next
        if B>=count:
            return A.next 
        
        temp=A
        for i in range(count-B-1):
            temp=temp.next
        
        if temp.next:
            temp.next=temp.next.next
        return A


        

