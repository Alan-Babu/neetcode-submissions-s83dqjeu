class Solution:
    def stringKey(self, item: str):
        count = [0]*26
        for char in item:
            count[ord(char)-ord('a')]+=1
        return tuple(count)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for items in strs:
            key = self.stringKey(items)
            hashmap.setdefault(key,[]).append(items)
        return list(hashmap.values())