class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        answer = [0] * len(arr) #create a ans array full of 0s with length arr

        for i in range(len(arr)):
            rightMax = -1
            for j in range(i+1, len(arr)):
                rightMax = max(rightMax, arr[j])
            answer[i] = rightMax  
        return answer

