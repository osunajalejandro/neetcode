class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
            
        buckets = [[] for _ in range(len(nums) + 1)]

        for key in freq:
            buckets[freq[key]].append(key)
        
        mostFrequentK = []

        for x in reversed(buckets):
            if len(mostFrequentK) == k:
                break
            if x:
                for item in x:
                    mostFrequentK.append(item)

        return mostFrequentK
        