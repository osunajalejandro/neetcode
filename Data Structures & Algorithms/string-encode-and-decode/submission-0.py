class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += str(len(s)) + "#" + s 
        return encodedStr

    def decode(self, s: str) -> List[str]:
        finalList = []

        i=0
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            j += 1

            word = s[j:j+length]
            finalList.append(word)

            i = j + length

        return finalList