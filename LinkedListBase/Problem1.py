# You are given A which is the head of a linked list. Print the linked list in space separated manner.

# Note : The last node value must also be succeeded by a space and after printing the entire list you should print a new line

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def solve(self, A):
        temp=A
        while temp:
            print(temp.val,end=" ")
            temp=temp.next 
        print()
