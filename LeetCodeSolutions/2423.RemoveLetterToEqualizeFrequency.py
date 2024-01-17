from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
    
        for char, count in counter.items():
            counter[char] -= 1
            uniqueCounts = set(val for val in counter.values() if val)

            if len(uniqueCounts) == 1:
                return True
            
            counter[char] += 1

        return False

