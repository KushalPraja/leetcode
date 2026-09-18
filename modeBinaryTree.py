class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        
        freq = {}

        def dfs(root):
            if not root:
                return

            if root.val not in freq:
                freq[root.val] = 0
            freq[root.val] += 1

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        mode = []
        max_so_far = 0

        for i,j in freq.items():
            if j > max_so_far:
                mode = [i]
                max_so_far = j
            
            elif j == max_so_far:
                mode.append(i)
            
        return mode
       
