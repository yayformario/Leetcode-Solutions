# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

#Using the class node that was given to us
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = None
        self.next = None

        

#val: [-5000,5000
#up to 5000 nodes

class iterativeSolution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
         #for readability
         currentNode = head

         pass

class interativeSolution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Going to need to pointers to traverse
        currentNode = head
        previousNode = None

        #Looping to the end
        while not (currentNode == None):
            #Store next node so we don't lose data
            nextNode = currentNode.next

            #can safely move nodes now
            currentNode.next = previousNode

            #Shift both previous and current nodes forward
            previousNode = currentNode
            currentNode = nextNode

        #PreviousNode is now head once everything is reversed
        return previousNode
    
class recursiveSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
            #Edge case where there's 0 nodes
            if not head:
                 return head
            
            #For readability
            currentNode = head

            #We want to loop until the end of the list
            if currentNode.next == None:
                return currentNode
            
            #Traverse deeper on each step until EOL
            #Popping is then in reverse order
            #Store each pop as the most recent endpoint
            oldEndPoint = self.reverseList(currentNode.next)

            #At this point, we move one step back
            #oldEndPoint == currentNode.next

            #With the endpoint saved, we can safely reverse the pointers
            nextNode = currentNode.next
            nextNode.next = currentNode

            #No longer need currentPointer to point to anything
            #Current pointer is now the end of the reversed linked list

            currentNode.next = None

            #return endPoint 
            return oldEndPoint
             

                  