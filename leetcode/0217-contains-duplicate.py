class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        for entry in nums:
            if entry in visited:
                return True
            visited.add(entry)
        
        return False