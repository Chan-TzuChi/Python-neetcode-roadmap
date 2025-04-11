# 題目：Contains Duplicate
# 類別：Arrays & Hashing
# 難度：Easy

# 問題描述（中英對照）：
# 給定一個整數陣列 nums，若其中有任何數值出現超過一次，請回傳 True，否則回傳 False。
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# 範例 1：
# Input: nums = [1, 2, 3, 3]
# Output: True

# 範例 2：
# Input: nums = [1, 2, 3, 4]
# Output: False

# 目標：確認陣列中是否有重複出現的數字
    # 回傳 True：如果有任一個數字出現超過一次
    # 回傳 False：如果全部都不重複

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# ✅ 測試：本地測試用（非 LeetCode）
if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1, 2, 3, 3]))  # True
    print(sol.hasDuplicate([1, 2, 3, 4]))  # False
