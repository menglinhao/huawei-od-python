#!/usr/bin/env python
# encoding: utf-8
"""
sorted 中 key 多级排序练习
"""

words = ["apple", "pen", "banana", "cat", "dog", "elephant", "book", "apple"]

# ===== 1. 统计词频后多级排序 =====
from collections import defaultdict

word_freqs = defaultdict(int)
for w in words:
    word_freqs[w] += 1

# key 返回一个元组，sorted 按元组元素优先级从左到右比较
# -x[1]:  词频降序（负号 = 反转方向）
# len(x[0]): 单词长度升序
# x[0]:   字典序升序
sorted_words = sorted(word_freqs.items(), key=lambda x: (-x[1], len(x[0]), x[0]))
print("多级排序结果:", sorted_words)

# ===== 2. 常见排序模式 =====

# 单级：按数字排序
nums = [3, 1, 4, 1, 5, 9]
assert sorted(nums) == [1, 1, 3, 4, 5, 9]

# 单级：按绝对值降序
nums2 = [-5, 3, -1, 4, -2]
assert sorted(nums2, key=abs, reverse=True) == [-5, 4, 3, -2, -1]

# 单级：按字符串长度
words2 = ["aaa", "bb", "cccc", "d"]
assert sorted(words2, key=len) == ["d", "bb", "aaa", "cccc"]

# 两级：先按长度，再按字典序
words3 = ["ccc", "bb", "aaa", "d", "ee"]
assert sorted(words3, key=lambda x: (len(x), x)) == ["d", "bb", "ee", "aaa", "ccc"]

# 混合升降：先按长度降序，再按字典序升序
assert sorted(words3, key=lambda x: (-len(x), x)) == ["aaa", "ccc", "bb", "ee", "d"]

# ===== 3. key 可以调用其他函数 =====
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student("alice", 90),
    Student("bob", 85),
    Student("charlie", 90),
]

# 先按成绩降序，再按名字升序
ranked = sorted(students, key=lambda s: (-s.score, s.name))
for s in ranked:
    print(f"  {s.name}: {s.score}")
assert [s.name for s in ranked] == ["alice", "charlie", "bob"]

# ===== 4. 等价写法：reverse vs 负号 =====
data = [("a", 3), ("b", 1), ("c", 2)]

# 写法A：key 里用负号控制某字段降序（可混合升降序）
by_neg = sorted(data, key=lambda x: -x[1])
# 写法B：reverse=True 全局降序（所有字段一起降）
by_rev = sorted(data, key=lambda x: x[1], reverse=True)
assert by_neg == by_rev  # 单级排序时等价

# 多级时负号才体现灵活性：先按数字降序，再按字母升序
data2 = [("b", 2), ("a", 2), ("c", 3)]
mixed = sorted(data2, key=lambda x: (-x[1], x[0]))
assert mixed == [("c", 3), ("a", 2), ("b", 2)]

print("\n全部断言通过 ✓")
