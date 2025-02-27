class Node:
    def __init__(self):
        self.index = None
        self.val = None
        self.next = None
        self.prev = None
        

class MyLinkedList:

    def __init__(self):
        #Start and end dummy nodes to minimize edge cases
        self.startNode = Node()
        self.endNode = Node()

        self.startNode.index = 'start'
        self.endNode.index = 'end'

        self.startNode.next = self.endNode
        self.endNode.prev = self.startNode

    """
    Get value at given index
    return -1 if not found
    """
    def get(self, index: int) -> int:
        #Search for the index
        #check if list is empty
        if self.startNode.next == self.endNode:
            return -1
        
        #Can return -1 if index is greater than our last node
        if index > self.endNode.prev.index:
            return -1
        
        #List exists and index isn't out of range
        #Gauranteed to find index
        traverse = self.startNode.next

        while not traverse == self.endNode:
            if traverse.index == index:
                return traverse.val
            traverse = traverse.next


        #Couldn't find it, somehow?
        return -1

    """
    Add val at the head
    """
    def addAtHead(self, val: int) -> None:

        #Check to see if the list is empty
        if self.startNode.next == self.endNode:
            #Just add temp to front
            tempNode = Node()
            tempNode.index = 0
            tempNode.val = val
            tempNode.prev = self.startNode
            tempNode.next = self.endNode

            #Adjust neighboring pointers
            self.startNode.next = tempNode
            self.endNode.prev = tempNode
            return None

        #Otherwise, gauranteed at least 1 node
        #Need to adjust their indicies
        traverse = self.startNode.next

        while not traverse == self.endNode:
            #Increase index since we're adding to front
            traverse.index += 1
            traverse = traverse.next

        #Once indicies are taken care of, add temp node to front
        #For readability
        left = self.startNode
        right = self.startNode.next

        tempNode = Node()
        tempNode.index = 0
        tempNode.val = val
        tempNode.prev = left
        tempNode.next = right

        #Adjust neighboring pointeres
        left.next = tempNode
        right.prev = tempNode
        return None

        

    """
    Add val at the end
    """
    def addAtTail(self, val: int) -> None:

        #Check to see if list is empty
        if self.endNode.prev == self.startNode:
            #Essentially adding to head
            self.addAtHead(val)
            return None

        #Gauranteed at least 1 node
        #For readability
        left = self.endNode.prev
        right = self.endNode

        #Can now adjust pointers
        newNode = Node()
        newNode.index = self.endNode.prev.index + 1
        newNode.val = val
        newNode.prev = left
        newNode.next = right

        #Adjust neighboring pointers
        left.next = newNode
        right.prev = newNode
        return None

    """
    Add value before index

    If index == len of list
        Add to end of list
    
        if index > len
            do nothing
    """
    def addAtIndex(self, index: int, val: int) -> None:

        #Check if list is empty
        if self.startNode.next == self.endNode:
            #Only adding to "end" if index is 0
            if index == 0:
                self.addAtTail(val)
            return None

        #Can check to see if index is too big
        if index > self.endNode.prev.index+1:
            #Do nothing
            return None
        
        #Can check to see if we add at the end
        if index == (self.endNode.prev.index + 1):
            #Add to end
            self.addAtTail(val)
            return None

        #Index should be in the list
        #List is not empty and index is not out of range
        else:
            #Loop until we find the index
            traverse = self.startNode.next

            #loop stops at endNode
            while not traverse == self.endNode:
                if traverse.index == index:
                    #If we find index; add the node right before it
                    #But first, prep the indicies for index and beyond
                    temp = traverse
                    while not temp == self.endNode:
                        temp.index += 1
                        temp = temp.next

                    #For readability
                    left = traverse.prev
                    right = traverse
                    
                    #Can safely add node right before index
                    temp = Node()
                    temp.index = traverse.index - 1 #need to offset since we +1'd everything
                    temp.val = val
                    temp.prev = left
                    temp.next = right

                    #Safely modify neighboring pointers
                    left.next = temp
                    right.prev = temp
                    return None

                traverse = traverse.next

            #Somehow couldn't find index?
            return None
    
    """
    Delete node if index is valid
    """
    def deleteAtIndex(self, index: int) -> None:
        #Check if list is empty
        if self.startNode.next == self.endNode:
            return None
        
        #Check to see if index is too big
        if index > self.endNode.prev.index:
            return None
        
        #List is not empty, and index isn't larger than list; it should exist to delete
        traverse = self.startNode.next
        
        #Stops at endNode
        while not traverse == self.endNode:
            if traverse.index == index:
                #Found the node to delete
                #Need to decrement indicies since we're deleting 
                temp = traverse
                while not temp == self.endNode:
                    temp.index -= 1
                    temp = temp.next

                #For readability
                left = traverse.prev
                right = traverse.next

                #Can safely rearrange pointers
                left.next = right
                right.prev = left

                #Clearing out traverse for good measure
                traverse = None

                #Return None
                return None
            
            traverse = traverse.next

        #somehow couldn't find index?
        return None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)

examples = [
    
    #Failed test case
    [
        ["MyLinkedList","addAtIndex","get"],
        [[],[1,0],[0]]
    ],

    [   
        ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"],
        [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    ],

    [
        ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
        [[], [1], [3], [1, 2], [1], [1], [1]]
    ],

    [
        ["MyLinkedList","addAtHead","deleteAtIndex"],
        [[],[1],[0]]
    ],


]

#Honestly, just making the object first

for i in range(len(examples)):
    instructions = examples[i][0]
    values = examples[i][1]
    linkedList = MyLinkedList()


    for j in range(1,len(instructions)):
        instruction = instructions[j]
        value = values[j]

        match instruction:
            case 'get':
                get = linkedList.get(value[0])
                print(get)
            case 'addAtHead':
                head = linkedList.addAtHead(value[0])
                print(head)
            case 'addAtTail':
                tail = linkedList.addAtTail(value[0])
                print(tail)
            case 'addAtIndex':
                index = linkedList.addAtIndex(value[0],value[1])
                print(index)
            case 'deleteAtIndex':
                delete = linkedList.deleteAtIndex(value[0])
                print (delete)




#
#obj = MyLinkedList()
#param_1 = obj.get(index)
#obj.addAtHead(val)
#obj.addAtTail(val)
#obj.addAtIndex(index,val)
#obj.deleteAtIndex(index)