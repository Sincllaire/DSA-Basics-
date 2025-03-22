class Node:
    def __init__(self, key, value):
        """
        Initialize a Node with a key, value, and reference to the next node.
        """
        self.key = key
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self, initial_capacity=10):
        """
        Initialize the Hashtable with a fixed initial capacity.
        """
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def put(self, key, value):
        """
        Add a key-value pair to the Hashtable.
        1. compute the index for which you would like to insert a new value
           -an operation that i will look up in my notes later for inserting a number or letter value cause theyre both different
        2.check the index(bucket) to see if the value you want to add can fit into the list 
        3. IF statement: if it is not free
        4. if the value you want has the SAME key, overwrite it to add it to the list
        5. if the value you want has a different key, it will be added under it and begin a chaining process
        """
        table = self.table
        index = hash(key) % len(self.table)

        if table[index] is None:
            table[index] = (key, value)

        elif table[index] != None:
                if table[index][0] == key:
                    table[index] = (key, value)

                else:
                    if isinstance(table[index], list):
                        table[index].append((key, value))
                    else:
                        table[index] = [table[index], (key, value)]

        pass

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        1. find the hash function using the formula: index = hash(key) % len(table). this will give you where the key value is being stored
        2. interate through the table[index] to see if the selected key value pair exists
        - if the table[index] != None, you will be then iterating through that bucket in order to find the key value pair
        - if the table[index] == None, you will need to print "key is not in the list"
        3. check to see if the bucket[index] is empty by iterating through the bucket
        - IF the bucket is full, key is there and exact, return the key

        """
        table = self.table
        index = hash(key) % len(self.table)
        if table[index] != None:
            for (stored_key, value) in table[index]:
                if stored_key == key:
                    return value
        else:
            print('key is not in the list')



        pass

    def remove(self, key):
        """
        Remove the key-value pair associated with the given key.
        Retrieve the value associated with the given key.
        1. find the hash function using the formula: index = hash(key) % len(table). this will give you where the key value is being stored
        2. interate through the table[index] to see if the selected key value pair exists
        - if the table[index] != None, you will be then iterating through that bucket in order to find the key value pair
        - if the table[index] == None, you will need to print "key is not in the list"
        3. check to see if the bucket[index] is empty by iterating through the bucket
        - IF the bucket is full, key is there and exact, remove it by doing table[index].remove((key, value))
        """
        table = self.table
        index = hash(key) % len(self.table)
        if table[index] != None:
            found = False
            for (stored_key, value) in table[index]:
                if stored_key == key:
                    found = True
                    table[index].remove((stored_key, value))
            if found == False:
                print('key is not in the list')
        else:
             print('key is not in the list')


        pass

    def size(self):
        """
        Return the current number of elements in the Hashtable.
        1. create a variable Count and set it equal to 0
        2. interate through table(table[bucket] is just a singular bucket) so that you can count how many values are stored
        3. you need an if statement: if there table[index] == None, dont increment the index
            -else(in order to handle chaining): count += len(table[index]) (not +=1 because thats not the whole of the table)
        4. after you finish iterating through the list, return count 

        """
        table = self.table
        index = hash(key) % len(self.table)
        count = 0
        if table[index] == None:
            return 0
        else:
            count += len(table[index])
        return count
        pass

    def is_empty(self):
        """
        Check if the Hashtable is empty.
        1. create a variable size
        2. iterate through the table
        3. if statement: if the variable size is == 0: return "table is empty"
            else: if size is > 0: return "table has keys"
        """
        table = self.table
        for bucket in table:
            if bucket is not None:
                var_size = len(bucket)
                if var_size = 0:
                    return f"table is empty."
                
        return "table is empty"
        pass

    def _hash(self, key):
        """
        Compute the hash index for a given key.
        1. use the hash function = hash(key) % len(table)
            -account for if there are no keys in the table
            - account for if there are no values in the table
        """
        if key is None:
            raise ValueError("key cannot be None")
        elif len(self.table) == 0:
            raise ValueError("Table cannot be empty")
            
        return hash(key) % len(self.table)
        pass

    def _resize(self):
        """
        Resize the Hashtable when the load factor exceeds a threshold.
        1. load_factor = size / len(table)
        2. you need to have another variable called thresh( the limit the table is supposed to have)
        3. after iterating through the list and counting the key you will need to create an if statement:
        - IF the load_factor > thresh: you need to 1. create a new table(new_table = [None] * (2 * len(table)))
                                            2. hash all key-value pairs to the new table by first iterating through the table
                                            3. table = new_table
        """
        thresh = 0.7
        elems = sum(1 for elem in self.table if elem is not None)
        load_factor = elems / len(self.table)

        if load_factor > thresh:
            new_table = [None] * (2 * len(self.table))
            
            for elem in self.table:
                if elem is not None:
                    key, value = elem
                    new_index = hash(key) % len(new_table)
                    

                    while new_table[new_index] is not None:
                        new_index = (new_index + 1) % len(new_table)
                        
                    new_table[new_index] = (key, value)

            self.table = new_table
            self.elems = elems
        pass

# Example Usage (for testing)
# hashtable = Hashtable()
# hashtable.put("key1", "value1")