class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
    
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        # Generate each row from the second row onward
        for i in range(1, numRows):
            prev_row = triangle[i-1]
            current_row = [1]
            
            # Compute the interior elements of the current row
            for j in range(1, i):
                current_row.append(prev_row[j-1] + prev_row[j])
            
            # The last element of each row is always 1
            current_row.append(1)
            
            # Add the current row to the triangle
            triangle.append(current_row)
        
        return triangle