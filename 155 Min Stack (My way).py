class MinStack(object):
    """
    Design a stack:
        Must complete the following in constant time:
            push, pop, top, getMin
    
    Functions:
        Minstack() initializes the stack object
        void push(int val) pushes the element val onto the stack
        void pop() removes the element on the top of the stack
        int top() gets the top element of the stack 
        int getMin() retrieves the minimum element in the stack
    """

    """
    Constraints:
    We can push negative integers onto the stack
        (-2^31) <= (val) <= (2^(31 - 1))

    The following are always called on non-empty stacks; no need to check for out of bounds:
        pop(), top(), getMin()

        - This essentially means that the first operation will always be a push() call
    
    At most, there will be 30,000 calls made to push, pop, top, and getMin
        (3 * 10^4)
    """

    """
    Approach:
        We initialize an empty stack when MinStack gets called

        Push is straight forward, we just append val to the stack

        Pop is also straight forward, we pop it from the stack

        Top essentially just gets the last value in the stack

    The tricky thing is managing getMin in constant time. 
        We can't compare it to pre-existing values; that will be O(n) time for each call
            This creates a terrible runtime of O(n^2) because we have to recompare after each call
            The program drastically slows down at higher inputs: 30k calls 

        We somehow need to know what the current minimum is when adding values

        Idea 1:
            Have a variable that keeps track of current minimum
                Problem: How will it know what the previous minimum was after a pop?
                We get stuck with the same issue of needing to compare previous values:

                    [10,8,-1]
                        min = -1
                    
                    After we pop():
                    [10,8]
                        min = -1

        Idea 2:
            We can create an array that keeps track of each iteration's current minimum 
                This kinda breaks apart if we add -> pop -> add 
                    How does the pointer crawl? 
                        It's possible to map pointer movements to each method:
                        push -> minPointer++ 
                        pop -> minPointer -- 
                        top -> minPointer doesn't move
                        getMin -> return stack[minPointer]
        
        Idea 3:
            We can initialize a second stack LOL 
                One stack that keeps track of our inputs
                The other stack keeps track of the current min value 
            
            Our runtime will still be O(n):
                We loop through the input once 
                    Push() Pop() Top() and minStack() are all O(2) 
                        We append twice
                        We pop twice
                        we top twice
                        getMin() will pop both but return minStack's value 
            
            Spacetime is O(2n) -> O(n)
                We're just managing two stacks, so double the memory space
                
    """
    def __init__(self):
        #Initialize two stacks: normal stack, minimum stack
        #minimum stack stores current minimum at the time; 
        #   Runtime: O(2)
        #   Spacetime: O(2) but each can grow to size n
        #       Worst case: Only appends until EOL; O(2n)
        self.normalStack = []
        self.minStack = [] 

    #Void push (int val)
    def push(self, val):
        """
        We're going to push our value to both stacks. 
        No return value needed
        """
        
        #Append value to the normal stack
        self.normalStack.append(val)

        #Append the current minimum value to minStack
        """
        We want to compare value to what's in our minStack. 
           EDGE CASE: Empty min stack? (First value)
           Check if min stack is empty; 
               Empty: Just append val
               Not Empty: Get the min of val and mins[-1]

        The if else statement can simplify to the following lines:
        # val = min(val, self.minStack[-1] if self.minStack else val)
        # self.minStack.append(val)

        Which can also simplify to one line:
        # self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
        """
        #Check to see if minStack is empty before appending
        if (self.minStack):
            # Compare given val with our currently stored min value in minStack
            # Append the min value of the two to minStack
            self.minStack.append(min(val, self.minStack[-1]))
        
        #If minStack is empty, simply append it
        else:
            self.minStack.append(val)

    #void pop()
    #Removes element on the top of the stack
    def pop(self):
        #Pop both stacks using the built in pop function
        self.normalStack.pop()
        self.minStack.pop()
    
    #Gets element on the top of the normal stack 
    def top(self):
        #We don't care about minstack here, just the normal stack
        return (self.normalStack[-1])
            
    #Retrieves the minimum element in the stack
    #Essentially we return the top value from our min stack
    def getMin(self):
        #Don't care about normalStack; just the minStack
        return self.minStack[-1]





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Provided example:
example = ["MinStack","push","push","push","getMin","pop","top","getMin"], [[],[-2],[0],[-3],[],[],[],[]]