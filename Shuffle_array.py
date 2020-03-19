

class Solution:
    
    def __init__(self, nums: List[int]):
        self.nums=nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        res = list(self.nums)
        random.shuffle(res)
        return res