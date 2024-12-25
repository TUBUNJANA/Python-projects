'''
***************************************************************************************
# Developer: TUBUN JANA
# Role: Backend Developer
# Company: [Your Company Name]
# Project: LRU Cache Implementation using Doubly Linked List
# Date Created: 25/12/24
# Last Updated: 25/12/24
# Time Spent: 3 hours
# Description: This class implements an LRU Cache using a Doubly Linked List 
# and a dictionary to efficiently handle caching and evicting least recently used 
# items when the cache exceeds its specified size.
*****************************************************************************************
'''

class DoubleLinkList:
    """
    Represents a node in a doubly linked list. This node stores the key-value
    pairs used by the LRU Cache. Each node has pointers to the previous and next nodes.
    """

    def __init__(self):
        """
        Initializes a node with default values.
        """
        self.key = -1        # Placeholder for the key
        self.value = -1      # Placeholder for the value
        self.previous = None # Points to the previous node
        self.next = None     # Points to the next node
    
    def printF(self):
        """
        Prints the current node's data (for debugging purposes).
        """
        print(f"({self.previous}, {self.key}, {self.value}, {self.next})")


class LruCache:
    """
    A Least Recently Used (LRU) Cache implemented using a doubly linked list
    and a dictionary. It allows efficient insertions, updates, and deletions,
    while evicting the least recently used item when the cache reaches its
    maximum capacity.
    """

    def __init__(self, sizeOfCache):
        """
        Initializes the LRU Cache with a fixed size and sets up a dummy head
        and tail for the doubly linked list.

        Args:
            sizeOfCache (int): The maximum number of items the cache can hold.
        """
        self.head = DoubleLinkList()  # Dummy head node
        self.tail = DoubleLinkList()  # Dummy tail node
        self.sizeOfCache = sizeOfCache  # Max cache size
        self.dictionary = {}  # Dictionary to store key-value pairs for quick access

        # Connect the dummy head and tail nodes
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache. 
        Moves the accessed node to the front (most recently used).

        Args:
            key (str): The key whose value is to be fetched.

        Returns:
            str | None: Returns the value if the key exists, otherwise None.
        """
        if key not in self.dictionary:
            return None  # Return None if the key is not in the cache
        else:
            node = self.dictionary.get(key)
            
            # If the node is already at the front, no need to move it.
            if self.head.next == node:
                return self.head.next.value
            else:
                # Remove the node from its current position
                node.previous.next = node.next
                node.next.previous = node.previous

                # Move the node to the front (most recently used position)
                node.previous = self.head
                node.next = self.head.next
                self.head.next = node
                node.next.previous = node

                return node.value
    
    def put(self, key, value):
        """
        Adds or updates the key-value pair in the cache. If the cache is full,
        it evicts the least recently used item to make room for the new item.

        Args:
            key (str): The key to be inserted/updated.
            value (str): The value to be associated with the key.
        """
        if len(self.dictionary) == self.sizeOfCache:
            # Cache is full, evict least recently used item
            if key in self.dictionary:
                self.__update(self.dictionary[key], value)  # Update the existing key
            else:
                self.__replace(key, value)  # Replace the least recently used item
        else:
            # Cache is not full, simply insert the new item
            if key in self.dictionary:
                self.__update(self.dictionary[key], value)  # Update the existing key
            else:
                self.__insertion(key, value)  # Insert a new key-value pair
    
    def delete(self, key):
        """
        Removes the key-value pair from the cache.

        Args:
            key (str): The key to be deleted.
        """
        if key not in self.dictionary:
            return None  # Return None if the key is not found
        node = self.dictionary.get(key)
        
        # Adjust pointers to remove the node from the doubly linked list
        previousNode = node.previous
        nextNode = node.next
        previousNode.next = nextNode
        nextNode.previous = previousNode

        # Also remove from dictionary
        del self.dictionary[key]
    
    def __replace(self, key, value):
        """
        Replaces the least recently used item (the node before the tail) with
        a new key-value pair.

        Args:
            key (str): The key of the new item.
            value (str): The value of the new item.
        """
        lastNode = self.tail.previous  # The least recently used node is just before the tail
        self.dictionary.pop(lastNode.key)  # Remove the old key from the dictionary
        lastNode.value = value  # Update the value of the evicted node
        lastNode.key = key  # Update the key of the evicted node
        self.dictionary[key] = lastNode  # Add the new key-value pair to the dictionary

    def __update(self, node, value):
        """
        Updates the value of an existing node in the cache and moves it to the front 
        (most recently used).

        Args:
            node (DoubleLinkList): The node to be updated.
            value (str): The new value for the node.
        """
        node.value = value  # Update the node's value
        # Move the node to the front to mark it as most recently used
        if node != self.head.next:
            node.previous.next = node.next
            node.next.previous = node.previous
            node.previous = self.head
            node.next = self.head.next
            self.head.next = node
            node.next.previous = node
    
    def __insertion(self, key, value):
        """
        Inserts a new key-value pair into the cache. The new node is placed at 
        the front of the list (most recently used).

        Args:
            key (str): The key of the new item.
            value (str): The value of the new item.
        """
        newNode = DoubleLinkList()  # Create a new node
        newNode.key = key
        newNode.value = value

        # Insert the new node at the front (immediately after the head)
        newNode.previous = self.head
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.next.previous = newNode
        self.dictionary[key] = newNode  # Add the new node to the dictionary

    def __str__(self):
        """
        Returns a string representation of the cache's contents.

        Returns:
            str: A string representation of all the key-value pairs in the cache.
        """
        head = self.head.next
        arr = "["
        while head != self.tail:
            arr += f"({head.key}, {head.value})"
            head = head.next
        arr += "]"
        return arr


# Example usage of LRU Cache:
cache = LruCache(3)  # Create a cache with capacity of 3
cache.put("key-1", "Value-1")  # Insert the first item
cache.put("key-2", "Value-2")  # Insert the second item
cache.put("key-3", "Value-3")  # Insert the third item

# Perform cache operations:
# cache.get("key-1")  # Fetch 'key-1'
# cache.get("key-2")  # Fetch 'key-2'
# cache.put("key-4", "Value-4")  # Evicts 'key-3'
# cache.put("key-3", "Value-New")  # Updates 'key-3'

cache.delete("key-2")  # Deletes 'key-2'
print(cache)  # Prints the current state of the cache: "[key-1, Value-1][key-3, Value-New]"
