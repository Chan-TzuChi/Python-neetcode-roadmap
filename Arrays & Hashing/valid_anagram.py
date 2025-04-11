# 題目：Valid Anagram
# 類別：Arrays & Hashing
# 難度：Easy

# 問題描述（中英對照）：
# 給定兩個字串 s 和 t，如果這兩個字串互為「字母重組詞」（anagram），則回傳 true，否則回傳 false。
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# 字母重組詞（anagram）是指由相同字母組成的字串，只是字母順序可以不同。
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# 範例 1：
# Input: s = "racecar", t = "carrace"
# Output: True

# 範例 2：
# Input: s = "jar", t = "jam"
# Output: False

# Constraints:
# 限制條件（Constraints）
# s and t consist of lowercase English letters.
# s 和 t 僅由小寫英文字母組成。

# 目標：確認兩個字串是否為「字母重組而成」（Anagram）
    # 回傳 True：如果兩個字串 由相同字母組成，且每個字母出現次數也完全相同
    # 回傳 False：如果兩個字串 長度不同，或是任一字母的出現次數不同


from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False

# ✅ 測試：本地測試用（非 LeetCode）
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram(s = "racecar", t = "carrace"))  # True
    print(sol.isAnagram(s = "jar", t = "jam"))  # False
