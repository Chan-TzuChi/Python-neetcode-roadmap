# 題目：Valid Anagram
- 類別：Arrays & Hashing
- 難度：Easy

---
### 筆記：
- Valid Anagram（有效的字母重組詞）：字母一樣、數量一樣、順序可以不同

---
🧰 方法一：使用 collections.Counter
 
```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

✅ 優點：
- 一行就能比較兩字串的字母統計
- Counter 會自動幫你統計每個字母出現幾次（key 為字母，value 為次數）

---
🧰 方法二：手動使用字典來統計（不使用套件）

🧠 解題思路：
1. 先比較長度：如果長度不同就直接回傳 False
2. 統計每個字母的出現次數
3. 逐一比對兩個字串中的字母頻率是否一致

```python
def isAnagram(s: str, t: str) -> bool:
    # 先比較長度：如果長度不同就直接回傳 False
    if len(s) != len(t):
        return False

    # 統計每個字母的出現次數
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1

    # 逐一比對兩個字串中的字母頻率是否一致
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
    return True
```

---
🧪用 s = "jar"、t = "jam" 這組輸入代回方法二的程式碼：
1. 先比較長度：如果長度不同就直接回傳 False
```python
    # len("jar") == 3, len("jam") == 3 → 通過

    if len(s) != len(t):
        return False
```
2. 統計每個字母的出現次數
-  建立字母統計表（count）for s = "jar"
```python
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
```
```python
    # 第一次迴圈 c = 'j'
      count.get('j', 0) 回傳 0，因為 'j' 還不存在 → 0 + 1 = 1
      # count = {'j': 1}
    
    # 第二次迴圈 c = 'a'
      count.get('a', 0) 回傳 0 → 0 + 1 = 1
      # count = {'j': 1, 'a': 1}
    
    # 第三次迴圈 c = 'r'
      count.get('r', 0) 回傳 0 → 0 + 1 = 1
      # count = {'j': 1, 'a': 1, 'r': 1}
```
3. 逐一比對兩個字串中的字母頻率是否一致
- 開始檢查 t = "jam" 的每一個字母
```python
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
```
```python
    # 第一次迴圈 c = 'j'
      if 'j' not in count:  # 'j' 存在，跳過
      count['j'] -= 1       # 1 → 0
      # count = {'j': 0, 'a': 1, 'r': 1}
    
    # 第二次迴圈 c = 'a'
      if 'a' not in count:  # 'a' 存在，跳過
      count['a'] -= 1       # 1 → 0
      # count = {'j': 0, 'a': 0, 'r': 1}
    
    # 第三次迴圈 c = 'm'
      if 'm' not in count:  # 'm' 不存在 → return False

```

---
🔍 .get() 是什麼？

語法：
```python
dict.get(key, default_value)
```
- 從字典中取出指定 key 對應的值，
- 如果該 key 不存在，就回傳預設值（default_value）

代回方法二：
```python
count = {}
for c in s:
    count[c] = count.get(c, 0) + 1
```
- 如果 count[c] 已經有值 → 加 1
- 如果 count[c] 沒有出現過 → 先給它預設值 0 再加 1

.get() 寫法等同於這樣寫：
```python
if c in count:
    count[c] += 1
else:
    count[c] = 1
```
