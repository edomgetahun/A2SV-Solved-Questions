class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        output = []
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_count.items():
            if len(output) < k:
                output.append(key)
        return output
