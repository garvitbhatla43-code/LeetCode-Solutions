class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        prev={}
        for i in range(0,len(nums)):
            if nums[i] in prev:
                prev[nums[i]]+=1
            else:
                prev[nums[i]]=1
        sorted_pairs=sorted(prev.items(),key=lambda x:x[1])
        sorted_dict=dict(sorted_pairs)
        all_keys=list(sorted_dict)
        required=all_keys[-k:]
        return required
        