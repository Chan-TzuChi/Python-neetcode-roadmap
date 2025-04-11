# 題目：Contains Duplicate
- 類別：Arrays & Hashing
- 難度：Easy

**筆記**：
- 使用 set 判斷是否有重複數字（查詢速度 O(1)）
- `set.add()` 是 set 的語法，加入元素；不會加入重複值
- `list.append()` 是 list 的語法，允許重複，查詢速度慢（O(n)）
  
```python
seen = set()
for num in nums:
    if num in seen:
        return True
    seen.add(num)
```

筆記補充

🔹 set() vs list 查詢效率
- set: 查詢元素是否存在 → 平均時間複雜度 O(1)
- list: 查詢元素是否存在 → O(n)，需逐一比較
→ 所以遇到「查重」情況時，優先選 set

🔹 set.add() vs list.append()
- set.add(x): 把元素加進 set，若已有該元素則不會重複加
- list.append(x): 加入元素到 list 結尾，允許重複
- set 是無序的，不保證加入順序；list 保有順序

✅ 解這題選 set 的原因是：
- 我們只在乎「是否重複出現」
- 不需要順序、不需要記錄位置
→ set 是最精簡快速的選擇

