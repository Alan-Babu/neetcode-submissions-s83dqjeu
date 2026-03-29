class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for val in strs:
            result+=str(len(val))+"#"+val
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            #find the seperator "#"
            j=i
            while s[j] != "#":
                j+=1
            #extract length
            length = int(s[i:j])

            #extract the string
            string = s[j+1:j+1+length]
            res.append(string) 

            #move pointer
            i = j+1+length
        return res          

