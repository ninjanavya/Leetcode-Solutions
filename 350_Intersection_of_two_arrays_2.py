class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq = {}

        for num in nums1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = []

        # Traverse nums2
        for num in nums2:
            if num in freq and freq[num] > 0:
                ans.append(num)
                freq[num] -= 1

        return ans