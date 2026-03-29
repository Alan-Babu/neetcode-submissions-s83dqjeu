from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)
        need = len(cnt)
        m = len(s1)

        for index, char in enumerate(s2):
            cnt[char]-=1
            if cnt[char] == 0:
                need-=1
            if index >= m:
                left = s2[index-m]
                cnt[left]+=1
                if cnt[left] == 1:
                    need+=1
            if need == 0:
                return True
        return False



        