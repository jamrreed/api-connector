

# create a tree
from api_connector.data_structures.tree import Tree, TreeNode

# root
root_node: TreeNode = TreeNode("root")

# level 1
level_one: list[TreeNode] = ((
    TreeNode("node-1"),
    TreeNode("node-2"),
    TreeNode("node-3")
))
root_node.children = level_one

# level 2
for node in level_one:
    node.children = list[TreeNode]((
        TreeNode("subnode-1"),
        TreeNode("subnode-2")
    ))

new_tree: Tree = Tree(root_node)

new_tree.print_nodes()