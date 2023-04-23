class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        
        # Iterate through each row of the matrix
        for i in range(len(accounts)):
            # Count the number of wealth in the row
            num_wealth = sum(accounts[i])
            # Add the row index and the number of wealth to the wealth list
            wealth.append((num_wealth, i))
        
        # Sort the wealth list by the number of wealth
        wealth.sort()
        
        # Return the indices of the k weakest rows
        return wealth[len(accounts)-1][0]