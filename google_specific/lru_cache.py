class DLLNode:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.max_capacity = capacity
        self.elements_in_cache_dict = {}
        self.curr_size_of_cache = 0
        self.dll_head = None
        self.dll_tail = None

    def get(self, key):
        if key in self.elements_in_cache_dict:
            node_obj = self.elements_in_cache_dict[key]
            self.move_node_to_tail(node_obj)
            return node_obj.data
        else:
            return -1

    def set(self, key, val):
        return self.update_or_insert_node(key, val)

    def remove_head(self):
        self.dll_head = self.dll_head.next
        self.dll_head.prev = None

    def insert_at_tail(self, new_tail_node):
        if self.dll_tail is None:
            # This is the first key value pair we store in cache
            self.dll_tail = new_tail_node
            self.dll_head = new_tail_node
            return

        self.dll_tail.next = new_tail_node
        new_tail_node.prev = self.dll_tail
        new_tail_node.next = None

        self.dll_tail = new_tail_node
        return

    def move_node_to_tail(self, node):
        if node == self.dll_tail:
            return

        if node == self.dll_head:
            self.remove_head()
            self.insert_at_tail(node)
            return

        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        self.insert_at_tail(node)

    def update_or_insert_node(self, key, val):
        # Check if this is a new key to be inserted into cache
        # It he key is already present we don't have to remove any elements from cache
        if key in self.elements_in_cache_dict:
            node_obj = self.elements_in_cache_dict[key]
            node_obj.data = val
            self.move_node_to_tail(node_obj)

        else:
            if self.curr_size_of_cache < self.max_capacity:
                node_obj = DLLNode(key, val)
                self.elements_in_cache_dict[key] = node_obj
                self.insert_at_tail(node_obj)
                self.curr_size_of_cache += 1
            else:
                self.remove_head()
                node_obj = DLLNode(key, val)
                self.elements_in_cache_dict[key] = node_obj
                self.insert_at_tail(node_obj)

    def print_lru_cache_order(self):
        node = self.dll_head

        print('\n', "Printing lru cache elements in reverse order (elements accessed most recently will come last)")

        while node is not None:
            print(node.key)
            node = node.next


lru = LRUCache(3)
print(lru.get('a'))
print(lru.set('a', 1))
print(lru.get('a'))
lru.print_lru_cache_order()
print(lru.set('b', 2))
print(lru.get('b'))
lru.print_lru_cache_order()
print(lru.get('a'))
print(lru.set('b', 12))
lru.print_lru_cache_order()
print(lru.set('c', 3))
print(lru.get('c'))
lru.print_lru_cache_order()
print(lru.set('d', 4))
print(lru.get('d'))
lru.print_lru_cache_order()
