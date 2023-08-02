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

        #Initialize an empty array to use as a stack
        stack = []

        #Loop entire list of operations
        for ops in operations:
            #Adds previous two scores
            if ops == "+":
                stack.append(stack[-1] + stack[-2])
            
            #Doubles last score
            elif ops == "D":
                stack.append(stack[-1] * 2)
            
            #Removes the last score
            elif ops == "C":
                stack.pop()

            #Add the new score     
            else:
                stack.append(int(ops))

        #Return the sum of the stack
        return sum(stack)
                
            

testing = Solution()

example1 = ["5","2","C","D","+"]
example2 = ["5","-2","4","C","D","9","+","+"]
example3 = ["1","C"]

print(testing.calPoints(example1))
print(testing.calPoints(example2))
print(testing.calPoints(example3))


