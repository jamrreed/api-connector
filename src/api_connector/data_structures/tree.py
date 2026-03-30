class TreeNode:
    def __init__(self, value: any = None):
        self.value = value
        self.children = []

class Tree:
    def __init__(self, root_node: TreeNode):
        self.root = root_node
        self.nodes = [root_node]

    def get_root(self) -> TreeNode:
        return self.root
    
    def get_all_nodes(self) -> list[TreeNode]:
        return self.nodes
    
    # method not really necessary
    def get_children(self, parent_node: TreeNode) -> list[TreeNode]:
        if parent_node not in self.nodes:
            raise ValueError("Chosen node is not present in this Tree.")
        
        return parent_node.children
        
    def add_child(self, parent_node: TreeNode, value: any) -> TreeNode:
        if parent_node not in self.nodes:
            raise ValueError("Node selected for adding child is not present in this Tree.")
        
        new_node = TreeNode(value)
        parent_node.children.append(new_node)

        return new_node
    
    def print_nodes(self):
        if self.root:
            print(self.root.value)
            current_children = self.root.children
            while current_children is not None and len(current_children) > 0:
                print_value = ""
                next_children = []
                for child in current_children:
                    print(child)
                    print_value += str(child.value) + " "
                    next_children.append(child.children)
                
                print(print_value.strip())
                current_children = next_children