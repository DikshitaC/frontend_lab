class PairSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_pair(self):
        num_dict = {}
        for index, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_dict:
                return num_dict[complement], index
            num_dict[num] = index
        return None

pair_sum = PairSum([2, 7, 11, 15], 9)
print(pair_sum.find_pair())
