class Node:
    def __init__(self):
        self.value = None
        self.prev = None
        self.next = None
class MyStack:

    '''
    implement LIFO stack using two queues
    push to back 
    peek/pop from front

    '''
    def __init__(self):
        #Two dummy nodes to minimize edge cases
        self.startNode = Node()
        self.startNode.value = 'start'

        self.endNode = Node()
        self.endNode.value = 'end'

        #Adjust pointers
        self.startNode.next = self.endNode
        self.endNode.prev = self.startNode
    
    '''
    pushes x to top of stack
    based on examples, top of stack is EOL
    '''
    def push(self, x: int) -> None:
        #Create temp
        temp = Node()
        temp.value = x

        #For readability
        left = self.endNode.prev
        right = self.endNode

        #Adjust pointers for temp
        temp.next = right
        temp.prev = left

        #Adjust other pointers
        left.next = temp
        right.prev = temp
        
    '''
    removes from top of stack
    based on examples, top of stack is EOL
    '''
    def pop(self) -> int:
        #Use the endNode to remove from top
        
        #Check if we can even pop
        if self.startNode.next == self.endNode:
            return -1
        
        #Grab lastNode and store the pointers
        lastNode = self.endNode.prev
        returnVal = lastNode.value

        #Unlink lastNode
        left = lastNode.prev
        right = lastNode.next 

        #Adjust pointers before deleting
        left.next = right
        right.prev = left

        #Delete last node
        lastNode = None

        #Return value
        return returnVal

    '''
    returns element top of stack
    '''
    def top(self) -> int:
        return self.endNode.prev.value
        
    '''
    return true if empty
    false by default
    '''
    def empty(self) -> bool:
        if self.startNode.next == self.endNode:
            return True
        
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

examples = [
    #Failed test case
    [
        ["MyStack","empty"],
        [[],[]]
    ],

    [
        ["MyStack", "push", "push", "top", "pop", "empty"],
        [[], [1], [2], [], [], []]
    ], 


]

for ex in examples:
    #Grab inputs
    commands = ex[0]
    inputs = ex[1]

    #Create an object for each set of examples
    testing = MyStack()

    #Loop the rest of the commands
    for i in range(1,len(commands)):
        command = commands[i]
        input = inputs[i]

        match command:
            case 'push':
                testing.push(input)
            case 'top':
                print(testing.top())
            case 'pop':
                print(testing.pop())
            case 'empty':
                print(testing.empty())