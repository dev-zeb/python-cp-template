from python_cp_template import TreeNode, preorder, inorder, postorder, bfs_tree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Preorder:")
preorder(root)
print("\nInorder:")
inorder(root)
print("\nPostorder:")
postorder(root)
print("\nBFS:")
bfs_tree(root)
