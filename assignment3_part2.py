class HashTable:
    """
    A Hash Table implementation that uses chaining (lists) for collision resolution.
    """
    
    def __init__(self, capacity):
        """
        Initializes the hash table with a given capacity.

        Args:
            capacity (int): The total number of buckets in the hash table.
        """
        self.capacity = capacity
        # Create empty buckets (lists) for chaining
        self.table = [[] for _ in range(capacity)]

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table. If the key already exists,
        its value is updated.

        Args:
            key: The key to insert or update.
            value: The data associated with the key.
        """
        # Find the index
        index = hash(key) % self.capacity
        
        # Check if key already exists, update if it does
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
                
        # If it's a new key, append it to the bucket
        self.table[index].append((key, value))

    def search(self, key):
        """
        Retrieves the value associated with a given key.

        Args:
            key: The key to search for.

        Returns:
            The value if the key is found, otherwise None.
        """
        index = hash(key) % self.capacity
        
        for k, v in self.table[index]:
            if k == key:
                return v
                
        return None

    def delete(self, key):
        """
        Removes a key-value pair from the hash table.

        Args:
            key: The key to be deleted.

        Returns:
            bool: True if the pair was successfully deleted, False if the key wasn't found.
        """
        index = hash(key) % self.capacity
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True # Successfully deleted
                
        return False # Key wasn't found
