class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        answer = [0] * len(arr) #create a ans array full of 0s with length arr

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1): #start = last element, stop = last element, step = -1 which is going backwards
            answer[i] = rightMax
            rightMax = max(rightMax, arr[i])
        
        return answer
