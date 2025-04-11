# 題目：Contains Duplicate
- 類別：Arrays & Hashing
- 難度：Easy

###筆記：
- 使用 set 判斷是否有重複數字（查詢速度 O(1)）
- `set.add()` 是 set 的語法，加入元素；不會加入重複值
- `list.append()` 是 list 的語法，允許重複，查詢速度慢（O(n)）
  
```python
# 建立一個空的集合 set，用來記錄「已經看過的數字」
# set 的查詢效率是 O(1)，比 list 快很多，適合用來檢查是否有重複
seen = set()

# 遍歷陣列中的每個數字
for num in nums:
    # 如果目前這個數字已經出現在 set 裡，代表出現過重複
    if num in seen:
        return True  # 發現重複，直接回傳 True

    # 如果沒有出現過，代表是第一次看到這個數字
    # 把它加入 set 中，以便之後可以檢查是否重複
    seen.add(num)

# 如果整個陣列都走完了，還沒遇到重複的數字
# 代表全部都不重複，回傳 False
return False
```

###筆記補充：

- `set()` 是一種無序且不重複的資料結構

✅ 解這題選 set 的原因是：
- 我們只在乎「是否重複出現」
- 不需要順序、不需要記錄位置
→ set 是最精簡快速的選擇


🆚 set() vs list 查詢效率
- set: 查詢元素是否存在 → 平均時間複雜度 O(1)
- list: 查詢元素是否存在 → O(n)，需逐一比較
→ 所以遇到「查重」情況時，優先選 set

🆚 set.add() vs list.append()
- set.add(x): 把元素加進 set，若已有該元素則不會重複加
- list.append(x): 加入元素到 list 結尾，允許重複
- set 是無序的，不保證加入順序；list 保有順序


❓為什麼在發現重複後直接 return？

- 題目只要求知道「是否存在重複」
- 一旦發現一個重複元素，就可以立刻終止程式，回傳 True
- 不需要繼續迴圈，這樣也節省執行時間

❓seen.add(num) 做什麼？

- 將當前元素記錄進 set 中
- 若該元素日後再次出現，就能透過 `if num in seen:` 檢查出來
