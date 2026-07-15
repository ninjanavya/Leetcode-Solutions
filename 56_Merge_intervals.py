class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]

        for intervals in intervals[1:]:
            if ans[-1][1] >= intervals[0]:
                ans[-1][1] = max(ans[-1][1], intervals[1])
            else:
                ans.append(intervals)

        return ans