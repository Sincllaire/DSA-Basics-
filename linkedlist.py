class Node:
    def __init__(self, data=None):
        """
        Initialize a Node with data and a reference to the next node.
        """
        #looked up how to initialize a node on geeks4geeks
        self.data = data
        self.next = next
        pass

class LinkedList:
    def __init__(self):
        """
        Initialize the LinkedList with a head node.
        """
        #the head is equal to none, because we dont have it set to anything yet 
        self.head = None

    def add(self, element):
        """
        Add an element to the end of the LinkedList.

        if list is empty, the heaed should be the new element
        if the list is already full, you want to go through the list and add it to the last node to add on the node at the end 
        """

        new_node = Node(element)
            
        if head == None:
            head = new_node
        else:
            current = head
            while current.next != None:
                current = current.next
            
        pass

    def insert(self, index, element):
        """
        Insert an element at the specified index.


        Logic Steps: Inserting New Node into a specific place
        -iterate through and stopping at the node which you want to insert the node after
                if head is none, head is new_node, else current is new node. 
                so it should be a while loop, while current != None, that updates current = current.next. ,
                then also updates the index_counter += 1, so for the head part, elif index ==0: head = new_node, 
                then for the next part we can delete the part about new_node.prev = current, then  new_node.next = current.next
            -you need to create a new node and have it have the attributes of data, also the index.(it was already assigned in the layout) 
            (new_node = node(data) || check 
            -you have to move the block before the new nodes pointer address to the new node you're inserting. the previous node has to now point to the new node || check
            -then you need to set the new_nodes pointer pointing to the node that the current node was previously pointing to.
            -make sure to update the previous nodes pointer to now point to the new node in which you added to the linked list
            -set the node that was previously the current node to point to new node, since it was moved to the right 
        
        -Use cases or things to think about/include:
            -you need to check to see if the new node is going before the head node
            -you need to check if the new node is going after the last node
        """
        new_node = Node(element, index) 

        if head == None:
            new_node.next = head
            head = new_node

        elif index == 0:
            new_node.next = head
            head = new_node


        else:
            current = head
            index_counter = 0


        while current != None and index_counter < index -1:
            current = current.next 
            index_counter += 1


        if current is not None:
            new_node.next = current.next
            current.next = new_node
         
        pass

    def get(self, index):
        """
        Retrieve the element at the specified index.

        you need to traverse through the linked list, 
        you need to determine what index youre going to stop at, 
        and have an index counter == index to stop, 
        return what you stop at, 
        and stop traversing through the list. 
        ( im just going to make up use cases cause there are none required) 
        use case one:check to see if the index is outside of the linked list amount,
        use case 2: if there is duplicates of the node 

        """
        if head == None:
            return None
            
        index_counter = 0
        current = head

        while current != None:
            
            if index_counter == index:
                
                return current.data 
            
            current = current.next 
            index_counter += 1
            
        return None
       

        pass

    def remove(self, index):
        """
        Remove the element at the specified index.

        Logic Steps:
        1. Iterate through the list
            a. traverse the list according to the index given that you want
                have to assign the current node to the head
                have to start the index counter at 0 
                if head == None:
                    return none Before the traversal
            b. stop at the given index
        2. you have your current node and your next node
                prev = None, before the loop 
            while loop to say that the index < target_index
        3. in order to remove the node, you have to modify the pointers and where they are pointing
                for your current node, you need to change your node next, to be node.next.next
                    prev.next = current.next
                    head = head.next if index == 0, if deleting the head and index is at 0
                    prev.next = None
        6. this should delete the node but not the node itself

        """


        if head == None:
            return None
        
        if target_index == 0:
            return head.next
            
        index_counter = 0
        current = head
        prev = None

        while index_counter < target_index:
            index_counter +=1
            prev = current
            current = current.next

        if current == None:
            return head
        
        prev.next = current.next
        

        pass


    def size(self):
        """
        Return the current number of elements in the LinkedList.

        1. before the code starts indentify the things that are constant through the list and go from head to the last node.
            if head == None:
                return 0
            index_counter = 0
            current = head
        2. keep track of how many nodes there are(traverse the nodes)
            while current != None:(makes sure to traverse every node)
                current = current.next
                
        3. return the size of the linkedlist 
            return index_counter
        """
        if head == None:
            return 0
        index_counter = 0
        current = head

        while current is not None:

            current = current.next
            index_counter +=1

        return index_counter


        pass

    def is_empty(self):
        """
        Check if the LinkedList is empty.

        1. need to count/ go through the loop 
            check to see if there are nodes in the list
            if head == None:
            return 0
        index_counter = 0
        current = head
        2. while current is not None:
            INdex_counter += 1 ( it will increment as it goes through the list)
            
        3. return the number from the index counter


        """
        if head == None:
            return 0
        index_counter = 0
        current = head
        while current is not None:
            index_counter += 1 
            current = current.next
        return index_counter




        pass

# Example Usage (for testing)
# linked_list = LinkedList()
# linked_list.add(5)