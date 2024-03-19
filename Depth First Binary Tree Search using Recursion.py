class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def dfs_recursive(root):
    if root is None:
        return
    # Process the current node
    print(root.val, end=" ")
    # Recur on the left subtree
    dfs_recursive(root.left)
    # Recur on the right subtree
    dfs_recursive(root.right)

# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print("Depth First Binary Tree Search (DFS) using recursion:")
dfs_recursive(root)
