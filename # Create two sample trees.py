# Create two sample trees
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# Check if the two trees are the same
print(is_same_tree(tree1, tree2))  # Output: True
