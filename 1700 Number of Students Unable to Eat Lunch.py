from typing import List


class Solution:
    '''
    sandwiches are in a stack
    students wait in a queue

    - if student likes the sandwich on top of the stack
        take the sandwhich and leave queue
    - else, student go to the queue's end

    -continues until none of the queue students want to take the top sandwich
    '''

    '''
    sandwhiches[i]
    students[j]

    i = 0 is the top of the stack
    j = 0 is the front of the queue
    '''

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #Don't really need a queue at all
        #Only the order of the sandwiches matter since it's a stack
        circles = 0
        squares = 0
        length = len(sandwiches)


        #Count all the students
        for student in students:
            if student == 0:
                circles += 1
            else: 
                squares += 1

        #Go down the stack
        for i in range(length):
            #Check if we have enough kids that want the sandwhich
            if sandwiches[0] == 0:
                #Check if we have enough zeros
                if circles == 0:
                    #Not enough kids
                    return len(sandwiches)
                else:
                    #Decrement and pop
                    circles -= 1
                    sandwiches.pop(0)
                    
            elif sandwiches[0] == 1:
                if squares == 0:
                    return len(sandwiches)
                else:
                    squares -= 1
                    sandwiches.pop(0)
        
        #Everyone got a sandwhich 
        return 0


examples = [
    #[students, sanwiches]
    [
        [1,1,0,0],
        [0,1,0,1]
    ],

    [
        [1,1,1,0,0,1],
        [1,0,0,0,1,1]
    ]
]

testing = Solution()

for ex in examples:
    students = ex[0]
    sandwiches = ex[1]
    x = testing.countStudents(students, sandwiches)
    print(x)
