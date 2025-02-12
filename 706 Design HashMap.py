
class Node:
    def __init__(self):
        self.key = None
        self.value = None

        self.left = None
        self.right = None


class linkedListHash:
    def __init__(self):
        self.start = Node()
        self.end = Node()

        #Fix pointers and add default keys
        self.start.right = self.end
        self.end.left = self.start
        self.start.key = 'start'
        self.end.key = 'end'

    def searchNode(self, key:int) -> Node:
        search = self.start

        while search.right.key != 'end':
            search = search.right
            if search.key == key:
                return search
        
        #Didn't find it, current node
        return search
        
        
    def put(self, key: int, value: int) -> None:
        #Search for the node
        node = self.searchNode(key)

        #Update the value if found
        if node.key == key:
            node.value = value

        #Add to our list if not found
        else:
            node = Node()
            node.key = key
            node.value = value

            #Adjust pointers
            oldLeft = self.end.left
            node.left = oldLeft
            node.right = self.end

            #Can safely update linked list
            oldLeft.right = node
            self.end.left = node

 

    def get(self, key: int) -> int: 
        #Search for node until it exists
        node = self.searchNode(key)

        #Return value if found
        if node.key == key:
            return node.value
        
        #Return -1 if not found
        else:
            return -1

    def remove(self, key: int) -> None:
        #Search for key
        #if found, fix pointers and delete
        node = self.searchNode(key)
        
        if node.key == key:
            #We need to remove it
            leftNode = node.left
            rightNode = node.right

            #Readjust pointers
            leftNode.right = rightNode
            rightNode.left = leftNode

            #Clear out the data on current node
            node.key = None
            node.value = None
            node.left = None
            node.right = None


class arrayHash:

    """
    MyHashMap() initializes the object with an empty map.
    at most 10^4 calls will be made
    """
    def __init__(self):
        #At most 10^4 calls will be made
        #Values can go up to 10^6
        #Creating an array so we can quickly find the index
        self.index = [None] * 1000000


        
        
    """
    void put(int key, int value) 
        inserts a (key, value) pair into the HashMap. 
        
        If the key already exists in the map, 
            update the corresponding value.

        Constraints:
            key >= 0
            value <= 10^6 
                negative values no limit?
    """
    def put(self, key: int, value: int) -> None:
        #if it DNE: add pair
        #else: update value
        #Value always gets updated tbh
        self.index[key] = value

    """
    int get(int key) 
        returns the value to which the specified key is mapped, 
            or -1 if this map contains no mapping for the key.
    """
    def get(self, key: int) -> int:
        if self.index[key] == None:
            return -1
        else:
            return self.index[key]
    """
    void remove(key) 
    if the map contains the mapping for the key.
        removes the key and its corresponding value 
    """
    def remove(self, key: int) -> None:
        #Just set it to empty
        if not (self.index[key] == None):
            self.index[key] = None



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



inputs = [
    [
        ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
        [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    ]
]

for input in inputs :
    #Initialize hashmap
    hash = linkedListHash()
    for i in range (1, len(input[0])):
        #Loop the inputs
        command = input[0][i]
        value = input[1][i] 

        match command:
            case 'put':
                hash.put(value[0],value[1])
                print('null')
            case 'get':
                temp = hash.get(value[0])
                print(temp)
            case 'remove':
                hash.remove(value[0])
                print('null')
            

