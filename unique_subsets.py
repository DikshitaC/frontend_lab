class Subsets:
    def __init__(self, nums):
        self.nums = nums

    def get_subsets(self):
        result = [[]]
        for num in self.nums:
            result += [item + [num] for item in result]
        return result

subsets = Subsets([1, 2, 3])
print(subsets.get_subsets())
