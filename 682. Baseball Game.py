class Solution (object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        """
        There are 4 possible operations:
            integer x: new score of x
            "+" - The sum of the previous two scores (gauranteed there will always be two previous scores)
            "D" - Doubles the previous score 
            "C" - Removes previous score from the record

        Return the sum of all the scores on the record
        """

        """
        Total Runtime: O(2n) 
            O(n) for looping entire list of operations
            O(n) for calculating sum of our stack

        Total Spacetime: O(n)
            O(n) for growing the stack
        """
        

        #Initialize an empty array to use as a stack
        #Runtime: O(1)
        #Spacetime: (1)
        stack = []

        #Loop entire list of operations
        #Runtime O(n)
        #Spacetime O(n) worst case
        for ops in operations:
            #Adds previous two scores
            #Runtime: O(1)
            #Spacetime: O(1)
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            
            #Doubles last score
            #Runtime: O(1)
            #Spacetime: O(1)
            elif ops == "D":
                stack.append(stack[-1] * 2)
            
            #Removes the last score
            #Runtime: O(1)
            #Spacetime: O(1)
            elif ops == "C":
                stack.pop()

            #Add the new score     
            else:
                stack.append(int(ops))

        #Return the sum of the stack
        #Runtime O(n)

        return sum(stack)
                
            

testing = Solution()

example1 = ["5","2","C","D","+"]
example2 = ["5","-2","4","C","D","9","+","+"]
example3 = ["1","C"]

print(testing.calPoints(example1))
print(testing.calPoints(example2))
print(testing.calPoints(example3))


