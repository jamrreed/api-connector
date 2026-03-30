class LinkedNode:
    def __init__(self, data: any):
        self.data = data
        self.next = None

class LinkedList:
    invalid_error_message = "Linked list is not formatted properly."
    def __init__(self, nodes: list[LinkedNode], first_node: LinkedNode):
        self.nodes = nodes
        self.first_node = first_node

        if not self._validate_list(self):
            raise ValueError(self.invalid_error_message)

    def _validate_list(self):
        if self.nodes and self.first_node:
            next_node_set = []
            ending_node_exists = False
            for node in self.nodes:
                if node.next is None:
                    # not valid if we encounter multiple None values for "next" nodes
                    # has more than 1 terminating node
                    if ending_node_exists:
                        return False
                    ending_node_exists = True

                # not valid if there are duplicate "next" entries
                # more than 1 node links to the same node
                if node.next in next_node_set:
                    return False
                
                # not valid if the next node does not exist in the nodes list
                if node.next not in self.nodes:
                    return False
                
                next_node_set.append(node.next)
    
    def AddNode(self, data: any):
        last_node_matches = [item for item in self.nodes if item.next is None]
        if len(last_node_matches) > 1:
            raise ValueError("Link list is corrupted - multiple ending nodes found.")
        elif len(last_node_matches) == 0:
            raise ValueError("Link list is corrupted - no ending nodes found.")
        else:
            new_node = LinkedNode(data)
            self.nodes.append(new_node)
            
            last_node = last_node_matches[0]
            last_node.next = new_node

    def RemoveNode(self, node: LinkedNode):
        if node not in self.nodes:
            pass
        
        # collect all items that would be considered the previous node of the node to remove
        matches_previous = [item for item in self.nodes if item.next is node]
        
        # link previous item to the next item after removed node
        if len(matches_previous) == 1:
            matches_previous[0].next = node.next
        # handle case of removing the first_node instance - no previous nodes exist
        elif len(matches_previous == 0):
            # the next node becomes the first node in the link as the current first will be removed
            self.first_node = node.next
        # fatal error - multiple links to a previous node
        else:
            raise ValueError("Link list is corrupted - multiple previous nodes linked to node being removed.")
        
        self.nodes.remove(node)

    def TraverseNodes(self, func_run: any) -> list[any]:
        ordered_data: list[any] = []
        if self.first_node:
            current_node: LinkedNode = self.first_node
            next_node: LinkedNode = self.first_node.next
            while current_node is not None:
                ordered_data.append(current_node.data)
                func_run(current_node.data, next_node.data)
                current_node = next_node
                next_node = current_node.next
        else:
            raise ValueError("Link list is corrupted - first node does not exist.")
        
        return ordered_data
