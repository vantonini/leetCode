class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = []
        
        # Iterate through each row of the matrix
        for i in range(len(mat)):
            # Count the number of soldiers in the row
            num_soldiers = mat[i].count(1)
            # Add the row index and the number of soldiers to the soldiers list
            soldiers.append((num_soldiers, i))
        
        # Sort the soldiers list by the number of soldiers
        soldiers.sort()
        
        # Return the indices of the k weakest rows
        return [soldiers[i][1] for i in range(k)]        