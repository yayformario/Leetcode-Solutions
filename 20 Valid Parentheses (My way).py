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
        Runtime: O(n) -> We only loop through s once if at all
        Spacetime: O(n) -> We potentially grow our stack to size n == len(s)
        
        Concept: Given a closing bracket, is it's matching opening bracket on top of the stack?
        """

        # Check to see if s.length is an odd value; 
        # automatically invalid as we're gauranteed an extra bracket
        #   Getting length is O(1) runtime
        #   Comparing using modulus is O(1) runtime
        if (len(s) % 2 != 0):
            return False

        # Create an empty stack to track brackets
        # Spacetime: O(n) -> Worst case it grows to (len of s)
        stack = []

        # Hashmap
        #   Key: Opening Brackets
        #   Value: Closing Brackets
        # Spacetime: O(1), 3 constants
        # --------------
        #  (  [  {
        #  )  ]  } 
        # --------------

        bracketsMap = {"(":")" , "[":"]", "{":"}"}

        # Loop entire string
        # Runtime: O(n)
        # Invalid if: (stack is empty) or (brackets do not match) 
        for bracket in s:
            # Check to see if have an opening bracket
            # These are automatically added to the stack
            if bracket in bracketsMap: #Runtime: O(1) search up
                #Runtime: O(1) to append 
                stack.append(bracket)

            # Otherwise we need to pop; some edge cases have an empty stack: 
            #   ") {"
            #
            # Check to see if the stack is empty; if so it's invalid
            # We can't pop from an empty stack due to out of bounds pop
            elif (not stack):
                return False

            #We can now safely pop from the stack to see if we have a matching bracket
            # We want to pop from the stack to get the top value: O(1) -> stack.pop()
            # Use that value to see if it matches our key (opening bracket): O(1)
            elif (bracket != bracketsMap[stack.pop()]):

            # Closing brackets get compared to top of stack's hashed value
                return False


        # At this point, if all brackets were matching, the stack should be empty
        # Returns true by default: if (not stack) has anything, it returns false
        return (not stack)
        

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