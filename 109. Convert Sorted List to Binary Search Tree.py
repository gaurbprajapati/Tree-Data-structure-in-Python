# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, start, end):
        if (start == end):
            return None

        if start.next == end:
            return TreeNode(start.val)

        slow = start
        fast = start.next.next
        while(fast != end and fast.next != end):
            fast = fast.next.next
            slow = slow.next
        midpoint = slow.next
        node = TreeNode(midpoint.val)
        node.left = self.solve(start, midpoint)
        node.right = self.solve(midpoint.next, end)
        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return head

        if not head.next:
            return TreeNode(head.val)

        return self.solve(head, None)

        '''

        if not head :
            return head
        
        if not head.next:
            return TreeNode(head.val)

        #finding mid
        #stoping one point befor the mid
        slow=head
        fast=head.next.next
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next

        #asigning mid 
        midpoint = slow.next
        node = TreeNode(midpoint.val)
        #cutting the join (dividing linkedlist )
        slow.next=None
        node.left  = self.sortedListToBST(head)
        node.right= self.sortedListToBST(midpoint.next)

        return node
'''
