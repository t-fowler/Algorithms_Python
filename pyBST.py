class pyBST_node:
    def __init__(self, data):
        self.left = None    # left child
        self.right = None   # right child
        self.size = 1       # number of nodes in subtree rooted here
        self.data = data

    def is_leaf(self):
        """Determines if the node is a leaf node i.e has no children."""
        return self.left is None and self.right is None
    
    def num_children(self):
        """Provides the number of children """
        ch = 0
        if self.left is not None:
            ch += 1
        if self.right is not None:
            ch += 1
        return ch

class pyBST:
    def __init__(self, compare_func, data = None):
        """Constructor for pyBST"""
        if data is None:
            self.root = None
        else:
            self.root = pyBST_node(data)
        self.compare = compare_func

    def is_empty(self):
        """Determines if the tree is empty."""
        return self.root is None
    
    def _is_empty(self, node):
        """Interval version for use on subtrees."""
        return node is None

    def size(self):
        """Returns the number of elements in the tree."""
        return self._size(self.root)
    
    def _size(self, node):
        """Interval version for use on subtrees."""
        if node is None:
            return 0
        return self._size(node.left) + self._size(node.right) + 1

    def height(self):
        """Returns the height of the tree."""
        return self._height(self.root)
    
    def _height(self, node):
        """Internal version for use on subtrees."""
        if node is None:
            return 0
        if node.is_leaf():
            # Case 1: leaf node.
            return 1
        elif node.left is None:
            # Case 2: one child.
            return self._height(node.right) + 1
        elif node.right is None:
            # Case 2: one child.
            return self._height(node.left) + 1
        else:
            # Case 3: two children.
            left = self._height(node.left)
            right = self._height(node.right)
            if left > right:
                return left + 1
            else:
                return right + 1

    def insert(self, new_data):
        """Inserts a new node into the tree."""
        self.root = self._insert(self.root, new_data)

    def _insert(self, node, new_data):
        """Internal version for use on subtrees."""
        if node is None:
            return pyBST_node(new_data)
        comp = self.compare(new_data, node.data)
        if comp < 0:    # new_data < node.data
           node.left = self._insert(node.left, new_data)
        elif comp > 0:  # new_data > node.data
            node.right = self._insert(node.right, new_data)
        else:
            return node
        node.size += 1
        return node

    def find(self, query):
        """Determines if a value is in the tree."""
        return self._find(self.root, query)

    def _find(self, node, query):
        """Internal version for use on subtrees."""
        if node is None:
            return False
        comp = self.compare(query, node.data)
        if comp == 0:
            return True # Hit
        elif comp < 0:
            # query is smaller. Check the left.
            return self._find(node.left, query)
        elif comp > 0:
            # query is larger. Check the right.
            return self._find(node.right, query)

    def in_order(self, mode = 0):
        """
        Returns a list containing the in order
        traversal of the binary search tree.
        """
        if mode:
            return [nd.data for nd in self._in_order(self.root)]
        return self._in_order(self.root)

    def _in_order(self, node):
        """Internal version for use on subtrees."""
        r = []
        if node is None:
            return r
        r += self._in_order(node.left)
        r.append(node)
        r += self._in_order(node.right)
        return r

    def pre_order(self, mode = 0):
        """
        Returns a list containing the pre order
        traversal of the binary search tree.
        """
        if mode:
            return [nd.data for nd in self._pre_order(self.root)]
        return self._pre_order(self.root)

    def _pre_order(self, node):
        """Internal version for use on subtrees."""
        r = []
        if node is None:
            return r
        r.append(node)
        r += self._pre_order(node.left)
        r += self._pre_order(node.right)
        return r

    def post_order(self, mode = 0):
        """
        Returns a list containing the post order
        traversal of the binary search tree.
        """
        if mode:
            return [nd.data for nd in self._post_order(self.root)]
        return self._post_order(self.root)

    def _post_order(self, node):
        """Internal version for use on subtrees."""
        r = []
        if node is None:
            return r
        r += self._post_order(node.left)
        r += self._post_order(node.right)
        r.append(node)
        return r
    
    def clear(self):
        """Clears the whole tree."""
        self.root = None

    def min(self):
        """Returns the minimum value in the tree."""
        if self.root is None:
            return None
        return self._min(self.root).data

    def _min(self, node):
        """
        Internal version for use on subtrees. 
        Returns a node instead of data value.
        """
        if node.left is None:
            return node
        else:
            return self._min(node.left)

    def delete_min(self):
        """Deletes the minimum value in the tree."""
        if self.is_empty():
            return
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        """Internal version for use on subtrees."""
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def remove(self, rem_data):
        """
        Removes the value rem_data from the tree.
        It is left to the caller to determine that
        the value is in the tree at the time of calling.
        """
        self.root = self._remove(self.root, rem_data)
        
    def _remove(self, node, rem_data):
        """
        Internal version for use on subtrees.

        The strategy is that this function returns the 
        same node object that it is passed. This node is 
        only changed if it is the node to be deleted. 
        It is then replaced with it's successor.
        """
        if node == None:
            return None
        comp = self.compare(rem_data, node.data)
        if comp == 0:
            # Node with 0 children: return None.
            # Node with 1 child: return the child.
            if node.left == None:   
                return node.right
            if node.right == None:
                return node.left
            # Node with 2 children: return the minimum node
            # in the right subtree.
            temp = node
            node = self._min(temp.right)
            node.right = self._delete_min(temp.right)
            node.left = temp.left
        elif comp < 0:
            node.left = self._remove(node.left, rem_data)
        else:
            node.right = self._remove(node.right, rem_data)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

        def show(self):
            """Prints a visual of the tree."""
            if self.is_empty():
                print("Empty Tree")
            curr_rank = 0
            ranks = [[self.root]]
            for rank in ranks:
                for node in ranks[curr_rank]:
                    pass
                    