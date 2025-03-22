class ArrayList:
    def __init__(self, initial_capacity=10):
        """
        Initialize the ArrayList with an initial capacity.
        """
        #We first have to initialize the array and its size at the beginning in order to give us things to use.
        # Also it is to have the starting elements at 0 and an empty array because we havent added anything yet. 

        self.initial_capacity = initial_capacity #initial capacity is initialized
        self.size = 0 # we havent aggregated any data to the size yet 
        self.array = [] #the array is empty

        pass

    def add(self, element):
        """
        Add an element to the end of the ArrayList.
        """
        # for the next step we have to add elements to the end of the array list using the append command. 
        # we are adding elements together with the append function
        #we then update the size of the array using += 1
        if self.size >= self.initial_capacity:
            self._resize()
        self.array.append(element)
        self.size += 1

        pass

    def insert(self, index, element):
        """
        Insert an element at the specified index.
        """
        #for the insert method, you have to insert the new element and the index in order to add in an element at a specified index
        if index < 0 or index > self.size:  #Prevent invalid index
            raise IndexError("Index out of bounds")
        
        if self.size >= self.initial_capacity:
            self._resize()
        self.array.insert(index, element)
        self.size += 1
        pass

    def get(self, index):
        """
        Retrieve the element at the specified index.
        """
        #we put index in square brackets because we are trying to retrieve the element from the array using self.array 
        if index < 0 or index >= self.size:  #Prevent invalid index
            raise IndexError("Index out of bounds")
        
        return self.array[index]

        pass

    def remove(self, index):
        """
        Remove the element at the specified index.
        """
        #use the pop function to remove an element from an array
        if index < 0 or index >= self.size:  # Fixed: Prevent invalid index
            raise IndexError("Index out of bounds")
        
        self.array.pop(index)
        self.size -= 1

        pass

    def size(self):
        """
        Return the current number of elements in the ArrayList.
        """
        #use the return call to return size 

        return self.size

        pass

    def is_empty(self):
        """
        Check if the ArrayList is empty.
        """
        #need to check if the array is empty by checking if the size of self is equal to 0
        #and if it is you need to say yes, that is true or no thats false.

        return self.size == 0


        pass

    def _resize(self):
        """
        Resize the internal array when capacity is reached.
        """
        #if the initial capacity is reached and increased beyond what it was in the beginning, 
        # you need to expand the array to be able to hold more elements
        # and double the initial capacity by adding a new empty list and multiplying it by the new initial capacity to double it 
        # None is used as a placeholder to say there is no actual elements in the new array and is a placeholder for future elements. 
        
        self.initial_capacity *= 2
        self.array.extend([None] * (self.initial_capacity - len(self.array)))
     
        pass
    
# Example Usage (for testing)
arr_list = ArrayList()

arr_list.add(5)
arr_list.insert(8, 2)
#arr_list.get(2)

#print(arr_list)

#End of problem questions
#1. What parts of the project did you get stuck on?
    #I got stuck on a lot of the different implementations for answers such as the size method and the resize method . I am also not too greate on using self, and different classes and things of that nature. Not saying i dont know it but Im very rusty.
#2. Why were you stuck?
    #I wanted to overcomplicate things and I am a little rusty on just reading the problem and making sure to not overthink it. Just lke the part on size. 
#3. What information did you need to get unblocked?
    # I really tried not to use outside information but I would put my answers into chatgpt and basically ask it ti say w or r(kind of like hotter or colder) if i was getting close to the answer or give me the right answer
    # along with give me hints or advice that didnt give me the answer. 
#4. How did you know you needed that information?
    # I didnt know I needed that answer until I would ask it for advice or would ask if im getting hotter or colder to the answer. 
    # I am trying to get out of the habit of using chatgpt and get more confident in me using my reasoning skills and critical thinking/coding knowledge to figure it out, but its been hard considering its being used like a crutch. 
#5. How did you find that information?
    #i used chatgpt and the help of websites like w3schools.com and stackabuse.com. Otherwise I was using my own knowledge. 
    # I feel guilty using chatgpt because I dont like to use it like a crutch to help me with the answer, I want to be able to reason through it, stop and think on my own about it. 

