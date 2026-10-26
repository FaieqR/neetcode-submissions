class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #One take run
        #create two variables, one for the count and the other for the result
        #Whenever we see a 1, we always increase count by 1, and 
        #When we see a 0, set result to compared max between current count and result, reset the count to 0
        #At the end return the max between the result and the count 

        result = 0
        count = 0

        for num in nums: 
            if num == 0:
                #compare the result with the count
                result = max(result, count)

                #reset count to 0 as we encountered a 0
                count = 0
            else:
                count += 1

        #return the max, because result is only set when we encounter a 0
        return max(result, count)
