from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #Review list comprehension. Created prefix grid with +1 to row and col
        #This is to quite literally to avoid edge cases
        #   We will be "chiseling" away the uneeded portions for our answer
        #   +1 to col and +1 to row helps avoid going out of bounds for the first row and first column cases
        self.prefixMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        #It's more useful for us later down the line to:
        #1. Calculate the prefixSum of the current row
        #2. Add the prefixSum value of the top row as we increment each column
        for r in range(ROWS):
            prefixSum = 0
            for c in range(COLS):
                #Prefix sum for each index as we usually would 
                prefixSum += matrix[r][c]

                #Add the prefixSum from the top row as we increment each column
                aboveSum = self.prefixMatrix[r][c + 1]

                #Offset coords by one when adding value to our prefixSum
                #   The extra +1 row will be on top
                #   The extra +1 col will be on the left
                #   These extra coords will always be 0 and are there for edge cases (adding and subtracting nothings)
                #       Keeps logic consistent across all test cases
                self.prefixMatrix[r+1][c+1] = prefixSum + aboveSum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #Offset the coordinates for easy reading 
        #Recall that our prefixSum is +1 in both col and row to minimize edge cases
        row1 = row1 + 1
        col1 = col1 + 1

        row2 = row2 + 1
        col2 = col2 + 1

        #Recall that the bottom right stores the total prefix sum of our "block"
        #Our desired sumRegion is inside this "block", but we need to chisel it out
        bottomRight = self.prefixMatrix[row2][col2]
        
        #Chisel everything that's above our desired sumRegion
        above = self.prefixMatrix[row1-1][col2]

        #Chisel everything that's to the left of our desired sumRegion
        left = self.prefixMatrix[row2][col1 - 1]

        #But we need to add back the (upper left) region that was removed twice (above and left chiseled it twice)
        topLeft = self.prefixMatrix[row1 - 1] [col1 - 1]

        #So our answer is:  (giant block) - (above region + left region) + (topLeft)
        return bottomRight - (above + left) + topLeft
    
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