class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}
        for i in range(len(nums)):
            if nums[i] not in freq_list:
                freq_list[nums[i]] = 1
            else:
                freq_list[nums[i]] += 1
        
        filtered_keys = sorted(freq_list, key=freq_list.get, reverse=True)
        return filtered_keys[:k]

    """
    using counter:
    from collections import counter
    freq = Counter(nums)
    return [x for x, count in freq.most_common(k)] 
    """
      