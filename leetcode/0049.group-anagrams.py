class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hash = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sorted_hash:
                sorted_hash[sorted_s].append(s)
            else:
                sorted_hash[sorted_s] = [s]
        
        return list(sorted_hash.values())

class Solution2:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_hash = {}

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            tupl = tuple(count)
            if tupl in sorted_hash:
                sorted_hash[tupl].append(s)
            else:
                sorted_hash[tupl] = [s]           
            
        return list(sorted_hash.values())