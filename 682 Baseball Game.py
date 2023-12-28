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
            "D" - Doubles the previous score (Gauranteed 1 previous score)
            "C" - Removes previous score from the record (Gauranteed 1 previous score)

        Return the sum of all the scores on the record
        """

        """
        Total Runtime: O(n + n) -> O(2n) -> O(n)
            O(n) for looping entire list of operations
            O(n) for calculating sum of our stack

        Total Spacetime: O(n)
            O(n) for growing the stack
                If all operations are int "x", then the stack can grow to size n
        """
        
        #Check to see if there's only 1 element
        #   "D" and "C" requires 2 elements; "+" requires 3 elements
        #   If operations is length of one; we're gauranteed an int to return
        #O(1) for getting length
        if len(operations) == 1:
            #O(1) for converting to int
            return int(operations[0])

        #Otherwise, initialize an empty array to use as a stack
        #Runtime: O(1)
        #Spacetime: O(1)
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
example4 = ["100"]

print(testing.calPoints(example1))
print(testing.calPoints(example2))
print(testing.calPoints(example3))
print(testing.calPoints(example4))