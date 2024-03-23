from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        rangeSum = 0
        #We only need to loops

        #Loops every row
        for row in range(row1, row2+1, 1):
            #Loops every column
            for col in range (col1, col2+1, 1):
                #Add current value to our rangeSum
                rangeSum += self.matrix[row][col]



        return rangeSum
    
#Given example
matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
testing = NumMatrix(matrix)
regions = [
     [2, 1, 4, 3], 
     [1, 1, 2, 2], 
     [1, 2, 2, 4]
]


for ex in regions:
    print(
        "Input: " + str(ex) + "\n" + 
        "Output: " + str(testing.sumRegion(ex[0], ex[1], ex[2], ex[3]))
    )

    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
    
"""
Constraints:
- Negative values need to be calculated
- Both cols and rows have the same constraints [1,200]
- The given coordinates of the sumRegion cannot be out of region and are bounded by:
    [0, m) for rows
    [0, n) for cols
    Basically... We don't have to account for the given sumRegion being out of bounds
"""