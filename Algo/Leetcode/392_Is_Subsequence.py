# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string 
# by deleting some (can be none) of the characters 
# without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index, ns, n = 0, len(s), len(t)
        for i in range(n):
            if index < ns and t[i] == s[index]:
                index+=1
        return True if index == ns else False
    
if __name__ == "__main__":
    s, t = "abc", "ahbgdc"
    expected = False
    solution = Solution()
    print(solution.isSubsequence(s, t) == expected)