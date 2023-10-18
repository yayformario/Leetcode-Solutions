class Solution (object):
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
        #   Key: Opening Brackets
        #   Value: Closing Brackets
        # Spacetime: O(1), 3 constants
        # --------------
        #  (  [  {
        #  )  ]  } 
        # --------------

        bracketsMap = {"(":")" , "[":"]", "{":"}"}


        #Loop entire string
        #Runtime: O(n) 
        for bracket in s:
            #Opening brackets are added to the stack
            if bracket in bracketsMap: #O(1) search up
                stack.append(bracket)

            #False if: (stack is empty) or (brackets do not match)
            #Check if stack is empty FIRST to avoid out of bounds
            #Closing brackets get compared to top of stack's hashed value
            elif (not stack) or (bracket != bracketsMap[stack.pop()]):
                return False


        #At this point, if all brackets were matching, the stack should be empty
        #Returns true by default: if (not stack) has anything, it returns false
        return (not stack)
        

testing = Solution()

example1 = "()"
example2 = "()[]{}"
example3 = "([{}])"
example4 = "}"

print(testing.isValid(example1))
print(testing.isValid(example2))
print(testing.isValid(example3))
print(testing.isValid(example4))