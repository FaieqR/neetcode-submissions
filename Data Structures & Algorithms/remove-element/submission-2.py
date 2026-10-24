class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Brute Force
        
        #Iterate through the whole list, skip any elements that match the target value and store the rest
        #Copy everything back into the original array (nums[i] = temp[i], replace each index value of nums with temp ones)
        #Return the length of temp


        temp = []

        for i in range(len(nums)):
            if nums[i] != val:
                temp.append(nums[i])
            
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return len(temp)
        



