class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        for i in range(len(mana)): 
            if i == 0: 
                start = 0
                prev = []
                currS = 0
                for s in skill:  
                    currS += s * mana[i]
                    prev.append(currS)
            else:  
                curr = []
                currS = 0
                for s in skill: 
                    currS += s * mana[i]
                    curr.append(currS)
                nextStart = prev[0]  
                for j in range(1, len(prev)):  
                    nextStart = max(nextStart, prev[j] - curr[j-1])
                for k in range(len(prev)):  
                    prev[k] = curr[k] + nextStart
        return prev[-1] 