class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def get_max_idx(value_list):
            max_idx = 0
            max_val = value_list[0]
            for idx, val in enumerate(value_list):
                if max_val < value_list[idx]:
                    max_val = value_list[idx]
                    max_idx = idx
            return max_idx
       
        top_elements = []
        num_set = set(nums)
        freq_dict = dict()
        for num in num_set:
            freq_dict[num] = 0
        for num in nums:
            freq_dict[num] += 1
        key_list = list(freq_dict.keys())
        value_list = []
        for key in key_list:
            value_list.append(freq_dict[key])
        for value in value_list:
            if len(top_elements) == k:
                break
            max_idx = get_max_idx(value_list)
            value_list[max_idx] = -1
            top_elements.append(key_list[max_idx])

        return(top_elements)



        

