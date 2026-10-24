class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Two Pointer intuition
        #Use a write pointer (k) to track where the next valid element should go
        #Whilst scanning through the list, if the current value does not equal to val, we write it position k and move k forward
    

        k= 0 #Tracks position of the next valid element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] #Replace the position of K in nums with the value of i 
                k += 1 #Increate the value of k 
        return k