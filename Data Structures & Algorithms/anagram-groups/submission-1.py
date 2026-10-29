from collections import Counter as counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = []
        answer = []
        for word in strs:
            arr = list(word)
            if counter(arr) not in words:
                words.append(counter(arr))
                answer.append([word])
            else:
                ind = words.index(counter(arr))
                answer[ind].append(word)
        return answer