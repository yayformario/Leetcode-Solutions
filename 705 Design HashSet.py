class Node():
    def __init__(self):
        self.key = None

        self.prev = None
        self.next = None


class LinkedListHash:

    def __init__(self):
        #Create a starting and ending node
        self.startNode = Node()
        self.endNode = Node()
        self.startNode.key = 'start'
        self.endNode.key = 'end'

        #Connect the pointers
        self.startNode.next = self.endNode
        self.endNode.prev = self.startNode
        
    def searchNode (self, key:int) -> Node:
        search = self.startNode

        while search.next.key != 'end':
            search = search.next
            if search.key == key:
                return search

        return search
    """
    Insert the value 'key' into the hashset
    """
    def add(self, key:int) -> None:
        
        node = self.searchNode(key)

        #Only add node if it doesn't exist
        if not (node.key == key):
            node = Node()
            node.key = key

            #For readability
            leftNode = self.endNode.prev
            rightNode = self.endNode

            #Attach new node
            node.prev = leftNode
            node.next = rightNode

            #Can safely adjust old pointers
            leftNode.next = node
            rightNode.prev = node


    """
    Removes value 'key' if it exists
    Does nothing if DNE
    """
    def remove(self, key: int) -> None:
        node = self.searchNode(key)

        #only remove the node if it exists
        if node.key == key:
            #For readability
            leftNode = node.prev
            rightNode = node.next

            #Adjust pointers
            leftNode.next = rightNode
            rightNode.prev = leftNode
            
            #Remove current value
            node.key = None
            node.prev = None
            node.next = None
    
    """
    Checks to see if key exists in hash or not
    """
    def contains(self, key: int) -> bool:
        node = self.searchNode(key)
        if node.key == key:
            return True
        return False

class arrayHash:

    def __init__(self):
        #Create an array for every potential value
        # 0 <= key <= 10^6
        #1 000 000 + 2 (zero inclusive)
        self.hash = [None] * 1000002

    def add(self, key: int) -> None:
        #only add if hash doesn't exist
        if self.hash[key] == None:
            self.hash[key] = key

    def remove(self, key: int) -> None:
        #Remove from hash
        if self.hash[key] == key:
            self.hash[key] = None
        

    def contains(self, key: int) -> bool:
        if self.hash[key] == key:
            return True
        
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



input = [
    [
        ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"],
        [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    ]
]


for ex in input:
    testing = arrayHash()
    for i in range(1,len(ex[0])):

        command = ex[0][i]
        key = ex[1][i]

        match command:
            case 'add':
                testing.add(key[0])
                print('null')
            case 'contains':
                result = testing.contains(key[0])
                print(result)
                
            case 'remove':
                testing.remove(key[0])
                print('null')
            
