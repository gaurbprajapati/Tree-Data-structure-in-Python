import collections
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, root, arr):
        q = collections.deque()
        q.append(root)
        ans = []
        while(q):
            qlen = len(q)
            sublist = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    sublist.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            ans.append(sublist)

        return ans[:-1]

#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         arr = []
#         return self.solve(root, arr)


nums = [1, 4, 7, 8, 5]

temp = nums[2:]
print(temp)

mx1 = min(temp)
temp.remove(mx1)

mx2 = min(temp)

print(mx1, mx2)
