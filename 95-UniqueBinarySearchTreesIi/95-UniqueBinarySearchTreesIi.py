# Last updated: 6/6/2026, 10:26:52 PM
class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        def generate(first, last):
            trees = []
            if first > last:
                return [None]

            for root in range(first, last + 1):
                for left in generate(first, root - 1):
                    for right in generate(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            return trees

        return generate(1, n)
