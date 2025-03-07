# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def linkedListConverter(self, array):
        #first element is the head
        head = ListNode()
        head.val = array[0]

        #The rest of the elements get linked
        traverse = head
        for i in range(1,len(array)):
            temp = ListNode()
            temp.val = array[i]

            traverse.next = temp
            traverse = temp

        return head


class Solution:
    def printTwinNode(self):
        n = 4
        #Printing all twin values to get a feel
        for i in range (n):
            twinVal = n - 1 - i
            print(i, twinVal)

    """
    Gauranteed 2 nodes
    [2,10^5]

    Gauranteed positive values
        [1,10^5]

    Twin:
    (n - 1 - i)
    """
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        #slow and fast pointer
        #twin values essentially 'repeat' twice
        #If we can get to middle of list, we can get all the twin pointers

        #fast and slow pointer to find middle of list
        slowPointer = head
        fastPointer = head

        reverseNode = None

        #Stops at last element of the list (t | f)
        while fastPointer and fastPointer.next:
            #Increment the fast pointer twice
            fastPointer = fastPointer.next.next
            
            #We want to reverse slow pointer as we move along
            nextPointer = slowPointer.next

            #Can now reverse the pointers
            slowPointer.next = reverseNode

            #Crawl reverseNode and slowPointer forward
            reverseNode = slowPointer
            slowPointer = nextPointer
        
        #Once we're free: 
        #   slowPointer should be 2nd middle
        #   reverseNode should be 1st middle 
        twinSum = 0
        #Stops after last pointer
        while slowPointer:
            twinSum = max(twinSum, slowPointer.val + reverseNode.val)

            slowPointer = slowPointer.next
            reverseNode = reverseNode.next

        return twinSum
            




#Convert to link list
examples = [
    #2 values
    [4,6],
    #4 values
    [4,2,2,3],
    #8 values
    [1,2,3,4,11,12,13,14],
    #16 values
    [1,2,3,4,11,12,13,14,1,2,3,4,11,12,13,14]

]

testing = Solution()

for ex in examples:
    #Convert to linked list
    linkedList = ListNode()
    linkedList = linkedList.linkedListConverter(ex)

    #pass the linked list into pair sum
    output = testing.pairSum(linkedList)

