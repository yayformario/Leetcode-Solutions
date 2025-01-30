"""
argument: int capacity
initialize LRU cache with positive size capacity
"""

"""
int get (int key)l O(1)
return value of key if it exists
return -1 otherwise
"""

class Node:
    #constructor class
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
       self.capacity = capacity
       self.currentCapacity = 0

       #Create a hashmap for our nodes
       #{ node.key : node }
       self.nodeCache = {}

       #Create start and end nodes
       self.start = Node('start',0)
       self.end = Node ('end', 0)

       #connect nodes
       self.start.next = self.end
       self.end.prev = self.start
       
    """
    int get(int key) 
    Return the value of the key if the key exists
    otherwise return -1.
    """
    def get(self, key: int) -> int:
        
        #Grabs the key if i
        if key in self.nodeCache:
            #This apparently counts as a 'use'
            #Disconnect and move node
            temp = self.disconnectNode(self.nodeCache[key])
            self.mostRecent(temp)
            return self.nodeCache[key].val
        
        else:
            return -1
        

    def disconnectNode(self, currentNode: Node) -> Node:
        #Always guaranteed a prev and next node
        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev

        #Can safely detach the curret node
        currentNode.prev, currentNode.next = None, None
        return currentNode
    

    def mostRecent(self, currentNode: Node) -> None:
        #Place currentNode as the most recent
        currentNode.next = self.end
        currentNode.prev = self.end.prev

        #Can safely correct the other nodes
        self.end.prev.next = currentNode
        self.end.prev = currentNode

    """

    void put(int key, int value) 
        Update the value of the key if the key exists. 
        Otherwise, add the key-value pair to the cache. 
        If the number of keys exceeds the capacity from this operation, 
            evict the least recently used key.

    Put has a handful of edge cases
        Are we at capacity?

        if at capacity:
                detatch least used node

        The node does not exist and needs to be added
            move node to most recent position

        The node exists and needs to be moved
            move node to most recent position

        
    """
    def put(self, key: int, value: int) -> None:
        
        #Check if node already exists
        temp = None

        if key in self.nodeCache:
            #Detatch the node so we can move it
            temp = self.disconnectNode(self.nodeCache[key])
            #update the value
            temp.val = value
        
        else:
            #Node does not exist, create the node
            temp = Node(key, value)
            self.currentCapacity += 1

        #Check if we're at capacity
        if self.currentCapacity > self.capacity:
            #Detatch least used node
            removedNode = self.disconnectNode(self.start.next)
            self.currentCapacity -= 1
            self.nodeCache.pop(removedNode.key)

        #We are ready to move the node
        self.mostRecent(temp)

        #Add the node to our cache
        self.nodeCache[key] = temp


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


examples = [
    [
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    ],
    [
        ["LRUCache","get","put","get","put","put","get","get"],
        [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
    ]
]

commands = examples[0][0]
inputs = examples[0][1]



#Loop commands for program
for example in examples:
    testing = LRUCache(inputs[0][0])

    for i in range(1, len(example[0])):
        #Grab the current command and input
        currentCommand = example[0][i]
        currentInput = example[1][i]

        #We can now do function calls
        match currentCommand:
            case 'put':
                testing.put(currentInput[0],currentInput[1])

            case 'get':
                grabbed = testing.get(currentInput[0])

            