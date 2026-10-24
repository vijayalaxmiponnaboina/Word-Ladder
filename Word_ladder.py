from collections import deque
class Solution:
    def differ_by_one(self,word1,word2):
        count=0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                count+=1
        return count
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        q=deque()
        ans=0
        visited=set()
        q.append(beginWord)
        visited.add(beginWord)
        
        while q:
            size=len(q)
            ans+=1
            for x in range(size):
                front=q.popleft()
                if front==endWord:
                    return ans
                for x in wordList:
                    if x not in visited:
                        val=self.differ_by_one(front,x)
                        if val==1:
                            q.append(x)
                            visited.add(x)
        return 0