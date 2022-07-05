# User function Template for python3

# design the class in the most optimal way
class DLLNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:

    # Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        self.cap = cap
        self.lru_cache_dict = {}
        # key : DLLNode
        self.dll_head = None
        self.dll_tail = None

    # Function to return value corresponding to the key.
    def get(self, key):
        if key not in self.lru_cache_dict:
            return -1

        else:
            key_node = self.lru_cache_dict[key]

            if key_node is not self.dll_tail:
                self.move_key_to_tail(key_node)

            return key_node.data

    # Function for storing key-value pair.   
    def set(self, key, value):
        if key not in self.lru_cache_dict:
            key_node = DLLNode(key, value)
            self.lru_cache_dict[key] = key_node

            if self.dll_tail:
                self.dll_tail.next = key_node
                key_node.prev = self.dll_tail
                self.dll_tail = key_node
            else:
                self.dll_head = self.dll_tail = key_node

            self.cap -= 1

            if self.cap < 0:
                self.remove_head_node()

        else:
            key_node = self.lru_cache_dict[key]
            key_node.data = value
            
        self.move_key_to_tail(key_node)

    def move_key_to_tail(self, node):
        prev_node = node.prev
        next_node = node.next

        # There is just one node in DLL
        if node == self.dll_head == self.dll_tail:
            return

        elif node == self.dll_head:
            self.dll_head = self.dll_head.next
            self.dll_tail.next = node
            node.next = None
            node.prev = self.dll_tail
            self.dll_tail = node

        elif node == self.dll_tail:
            return

        else:  # This is some node in the middle (not head node, not tail node)
            prev_node.next = next_node
            next_node.prev = prev_node

            self.dll_tail.next = node
            node.next = None
            node.prev = self.dll_tail
            self.dll_tail = node

    def remove_head_node(self):
        self.dll_head = self.dll_head.next
        self.dll_head.prev = None
        return

