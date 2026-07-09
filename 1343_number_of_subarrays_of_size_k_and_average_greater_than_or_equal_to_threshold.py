class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #sum
        window_sum = sum(arr[:k])
        count = 0
        target = threshold*k

        #check
        if window_sum >= target:
            count += 1
        #slide
        for i in range(k,len(arr)):
            window_sum = window_sum-arr[i-k]+arr[i]
            if window_sum >= target:
                count += 1
        return count
        