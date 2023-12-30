class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        Only given the following characters:
            '()[]{}'

        An input string is valid if:
            Open brackets must be closed by the same type of brackets
            Open brackets must be closed in the correct order
            Every close bracket has a corresponding open bracket of the same type
        """

        
        """
        Stack and Hashmap approach
        
        Concept: Given a closing bracket, is it's matching opening bracket on top of the stack?
        """
        
        #Create an empty stack to track brackets
        #Spacetime: O(n) (len of s)
        stack = []

        #Hashmap
        #   Key: Closing Brackets
        #   Value: Open Brackets
        # Spacetime: O(1), 3 constants
        # --------------
        #  )  ]  }
        #  (  [  { 
        # --------------

        myMap = {")":"(" , "]":"[", "}":"{"}


        #Loop entire string
        #Runtime: O(n) 
        for bracket in s:
            #Open Brackets DNE as keys in our hashmap
            if bracket not in myMap: #O(1) search up
                stack.append(bracket)
                continue
            if not stack or stack[-1] != myMap[bracket]:
                return False
            stack.pop()


        #return true by default
        return not stack
        

testing = Solution()

#=====--- Valid Edge Cases ---=====#
example1 = "()"
example2 = "()[]{}"
example3 = "([{}])"

#=====--- Invalid Edge Cases ---=====#
#Opening brackets only
example4 = "({[({[["  

#Closig brackets only
example5 = ")}])]))}]]"

#Length of 1
example6 = "}"

#Out-of-order brackets
example7 = "]["
example8 = "){"
example9 = "([}{])"
example10 = "()[]}{()"


print(testing.isValid(example1))
print(testing.isValid(example2))
print(testing.isValid(example3))
print(testing.isValid(example4))
print(testing.isValid(example5))
print(testing.isValid(example6))
print(testing.isValid(example7))
print(testing.isValid(example8))
print(testing.isValid(example9))
print(testing.isValid(example10))