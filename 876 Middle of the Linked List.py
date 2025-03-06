# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from sandbox.etc import ListNode


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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #Can use a slow and fast pointer solution
        slowPointer = head
        fastPointer = head
        
        

        #As soon as the fast pointer hits EOL, slow pointer is at middle
        while fastPointer:

            #We want to move fastPointer first
            for i in range (2):
                if fastPointer.next:
                    fastPointer = fastPointer.next
                else:
                    #If we're at EOL, check if even or odd list
                    #Odd list, slow pointer is always in middle
                    if i == 0:
                        return slowPointer.val
                    #Even list, take the second middle node
                    else:
                        return slowPointer.next.val

                
            slowPointer = slowPointer.next

            

        return slowPointer.val
    


examples = [
    #One element
    [1], #1
    # Two elements
    [1,2], #2

    #given examples
    [1,2,3,4,5], #3
    [1,2,3,4,5,6] #4
]

for ex in examples:
    #Convert to linkedList
    linkedList = ListNode()
    linkedList = linkedList.linkedListConverter(ex)

    #Create middleNode 
    testing = Solution()

    #check for middleNode
    output = testing.middleNode(linkedList)
    print(output)

    