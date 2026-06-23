#!/usr/bin/env python
# encoding: utf-8
"""
codes/ 中不常用函数/方法练习
"""

# ===== 1. bin / hex / oct / int(x, base) =====
# 十进制 ↔ 二进制/十六进制/八进制
num = 42
assert bin(num) == "0b101010"        # → 二进制字符串
assert hex(num) == "0x2a"            # → 十六进制
assert oct(num) == "0o52"            # → 八进制

# bin(num)[2:] 去掉 0b 前缀
assert bin(num)[2:] == "101010"
# int(string, base) 转回十进制
assert int("101010", 2) == 42
assert int("2a", 16) == 42
assert int("0x2a", 16) == 42        # 0x 前缀也能识别
assert int("52", 8) == 42

# 位运算
assert 42 & 0b111111 == 42          # 按位与
assert 42 | 0 == 42                 # 按位或
assert 42 ^ 0b111111 == 21          # 按位异或（42=101010, 63=111111 → 010101=21）
assert 42 >> 1 == 21                # 右移 = //2
assert 42 << 1 == 84                # 左移 = *2

print("1. bin/hex/oct/int OK")


# ===== 2. ord / chr =====
# 字符 ↔ Unicode 码点
assert ord("A") == 65
assert ord("a") == 97
assert ord("0") == 48
assert chr(65) == "A"
assert chr(97) == "a"

# 常见用法：字母转数字索引
c = "C"
assert ord(c) - ord("A") == 2       # 'C' 是第 3 个大写字母（索引 2）

# 小写字母循环移位
def shift_char(c: str, offset: int) -> str:
    """字母循环右移 offset 位"""
    return chr((ord(c) - ord("a") + offset) % 26 + ord("a"))

assert shift_char("a", 1) == "b"
assert shift_char("z", 1) == "a"

print("2. ord/chr OK")


# ===== 3. zip =====
# 并行遍历多个可迭代对象
a = [1, 2, 3]
b = ["x", "y", "z"]
c = [True, False, True]

# 同时遍历
zipped = list(zip(a, b, c))
assert zipped == [(1, "x", True), (2, "y", False), (3, "z", True)]

# 解压
nums, chars, flags = zip(*zipped)   # * 展开 → zip( (1,x,T), (2,y,F), (3,z,T) )
assert nums == (1, 2, 3)
assert chars == ("x", "y", "z")

# 生成字典
keys = ["name", "age"]
vals = ["alice", 25]
assert dict(zip(keys, vals)) == {"name": "alice", "age": 25}

# 逐元素计算
x = [1, 2, 3]
y = [4, 5, 6]
assert [i + j for i, j in zip(x, y)] == [5, 7, 9]

# 长度不等时以最短为准
short = [1, 2]
long = [10, 20, 30]
assert list(zip(short, long)) == [(1, 10), (2, 20)]

print("3. zip OK")


# ===== 4. enumerate =====
items = ["a", "b", "c"]
# 基础：同时拿索引和值
for i, v in enumerate(items):
    pass
assert list(enumerate(items)) == [(0, "a"), (1, "b"), (2, "c")]

# start 指定起始序号
assert list(enumerate(items, start=1)) == [(1, "a"), (2, "b"), (3, "c")]

# 常用：构建带原始位置的列表
nums = [30, 10, 20]
indexed = [(n, i) for i, n in enumerate(nums)]
sorted_indexed = sorted(indexed)    # 按值排序，位置信息保留
assert sorted_indexed == [(10, 1), (20, 2), (30, 0)]

print("4. enumerate OK")


# ===== 5. filter / map / reduce =====
# filter: 保留使函数返回 True 的元素
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
assert even == [2, 4, 6]
# filter(None, ...) 过滤掉 false 值
assert list(filter(None, [0, 1, "", "a", None, [], [1]])) == [1, "a", [1]]

# map: 对每个元素应用函数
squared = list(map(lambda x: x**2, nums))
assert squared == [1, 4, 9, 16, 25, 36]
# map 多参数
a, b = [1, 2, 3], [10, 20, 30]
assert list(map(lambda x, y: x + y, a, b)) == [11, 22, 33]

# reduce: 累积归约（必须 import）
from functools import reduce
# 连乘
assert reduce(lambda x, y: x * y, [1, 2, 3, 4]) == 24
# 等价于 (((1 * 2) * 3) * 4)

# 有初始值
assert reduce(lambda x, y: x + y, [1, 2, 3], 10) == 16  # 10 + 1 + 2 + 3

print("5. filter/map/reduce OK")


# ===== 6. any / all =====
# any: 任一为 True 则 True
assert any([False, False, True]) == True
assert any([False, False, False]) == False
assert any([]) == False             # 空序列为 False

# all: 全为 True 才 True
assert all([True, True, True]) == True
assert all([True, False, True]) == False
assert all([]) == True              # 空序列为 True（vacuously true）

# 实战：检查字符串是否全为数字
s = "12345"
assert all(c.isdigit() for c in s)
# 检查是否有大写字母
s2 = "abcDe"
assert any(c.isupper() for c in s2)

print("6. any/all OK")


# ===== 7. itertools =====
import itertools

# combinations: 无序组合 C(n,k)，无重复
items = [1, 2, 3, 4]
assert list(itertools.combinations(items, 2)) == [
    (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)
]
# C(4,2) = 6 种

# permutations: 有序排列 P(n,k)，顺序不同算不同
assert len(list(itertools.permutations(items, 2))) == 4 * 3  # = 12

# product: 笛卡尔积
colors = ["红", "黑"]
suits = ["♥", "♠"]
assert list(itertools.product(colors, suits)) == [
    ("红", "♥"), ("红", "♠"), ("黑", "♥"), ("黑", "♠")
]
# product(*lists) 用于多个列表的组合
lists = [[1, 2], ["a", "b"]]
assert list(itertools.product(*lists)) == [
    (1, "a"), (1, "b"), (2, "a"), (2, "b")
]

# chain: 展平多层可迭代对象
nested = [[1, 2], [3, 4], [5]]
assert list(itertools.chain(*nested)) == [1, 2, 3, 4, 5]
# 等价于
flat = [x for sub in nested for x in sub]
assert flat == [1, 2, 3, 4, 5]

print("7. itertools OK")


# ===== 8. collections =====
from collections import Counter, defaultdict, deque

# --- Counter: 统计频次 ---
words = ["a", "b", "a", "c", "b", "a"]
cnt = Counter(words)
assert cnt == Counter({"a": 3, "b": 2, "c": 1})
assert cnt["a"] == 3
assert cnt.most_common(2) == [("a", 3), ("b", 2)]  # 前 2 高频
# Counter 之间可以加减/交并
c1 = Counter("aab")
c2 = Counter("abc")
assert c1 + c2 == Counter({"a": 3, "b": 2, "c": 1})   # 加
assert c1 - c2 == Counter({"a": 1})                     # 减
assert c1 & c2 == Counter({"a": 1, "b": 1})            # 交（取 min）
assert c1 | c2 == Counter({"a": 2, "b": 1, "c": 1})   # 并（取 max）

# --- defaultdict: 带默认值的字典 ---
# defaultdict(int): 访问不存在的 key 时自动初始化为 0
freq = defaultdict(int)
for ch in "hello":
    freq[ch] += 1   # 不需要 if ch not in freq
assert freq == {"h": 1, "e": 1, "l": 2, "o": 1}

# defaultdict(list): 自动初始化为空列表
groups = defaultdict(list)
groups["even"].append(2)
groups["even"].append(4)
groups["odd"].append(1)
assert groups == {"even": [2, 4], "odd": [1]}

# --- deque: 双端队列 ---
dq = deque([1, 2, 3])
dq.append(4)        # 右侧加 → [1,2,3,4]
dq.appendleft(0)    # 左侧加 → [0,1,2,3,4]
assert dq.pop() == 4       # 右侧弹出
assert dq.popleft() == 0   # 左侧弹出
assert list(dq) == [1, 2, 3]
# BFS 常用: queue = deque([start]); while queue: node = queue.popleft()

print("8. collections OK")


# ===== 9. heapq (小顶堆) =====
import heapq

nums = [3, 1, 4, 1, 5]
# heapify: 原地建堆
heapq.heapify(nums)
assert nums[0] == 1            # 堆顶永远是最小值

# heappush: 入堆
heapq.heappush(nums, 0)
assert nums[0] == 0

# heappop: 弹出最小值
assert heapq.heappop(nums) == 0

# nsmallest / nlargest: 不修改原数据的 topK
data = [5, 1, 9, 2, 7]
assert heapq.nsmallest(2, data) == [1, 2]
assert heapq.nlargest(2, data) == [9, 7]

# 大顶堆技巧：存负数
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)
assert -heapq.heappop(max_heap) == 5  # 弹出的是最大值的负数

print("9. heapq OK")


# ===== 10. re 正则 =====
import re

text = "订单号: OD12345, 金额: 99.5元"

# findall: 返回所有匹配的列表
assert re.findall(r"\d+", text) == ["12345", "99", "5"]  # \d+ 连续数字

# search: 找第一个匹配，返回 Match 对象
m = re.search(r"OD(\d+)", text)     # () 捕获组
if m != None:
    assert m.group(0) == "OD12345"      # 完整匹配
    assert m.group(1) == "12345"        # 第一个捕获组

# compile: 预编译模式（重复使用时高效）
p = re.compile(r"[a-zA-Z]+")        # 连续字母
assert p.findall("abc123def") == ["abc", "def"]

# sub: 替换
assert re.sub(r"\d+", "X", "a1b23c") == "aXbXc"

# 字符类
assert re.findall(r"[aeiou]+", "hello world") == ["e", "o", "o"]  # 元音
assert re.findall(r"[^aeiou]+", "hello") == ["h", "ll"]  # 非元音
assert re.findall(r"\w+", "hi, bye!") == ["hi", "bye"]   # \w = [a-zA-Z0-9_]

print("10. re OK")


# ===== 11. math 常用 =====
import math

assert math.gcd(12, 8) == 4          # 最大公约数
assert math.ceil(3.1) == 4           # 向上取整
assert math.floor(3.9) == 3          # 向下取整
assert math.isqrt(10) == 3           # 整数平方根（向下取整）
assert math.log2(8) == 3.0           # log2
assert math.log(100, 10) == 2.0      # log10(100)

# 进制转换辅助
assert math.ceil(math.log2(1000)) == 10  # 1000 需要 10 位二进制表示

print("11. math OK")


# ===== 12. 综合练习 =====
# 场景：给字符串 "a3b2c4"，展开为 "aaabbcccc"
def expand(s):
    pairs = zip(s[::2], s[1::2])          # zip 配对
    return "".join(ch * int(n) for ch, n in pairs)
assert expand("a3b2c4") == "aaabbcccc"

# 场景：检查两个单词是否为字母异位词
def is_anagram(w1, w2):
    return Counter(w1) == Counter(w2)
assert is_anagram("listen", "silent")
assert not is_anagram("hello", "world")

# 场景：寻找列表中和为 target 的所有数对（index 组合）
def find_pairs(nums, target):
    result = []
    for i, j in itertools.combinations(range(len(nums)), 2):
        if nums[i] + nums[j] == target:
            result.append((i, j))
    return result
assert find_pairs([2, 7, 11, 15], 9) == [(0, 1)]

# 场景：用 reduce 计算阶乘
'''
from functools import reduce
result = reduce(function, iterable, initializer)
'''
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
assert factorial(5) == 120

# 场景：判断列表中是否所有元素都满足条件，且至少有一个满足另一个条件
data = [2, 4, 6, 8]
assert all(x % 2 == 0 for x in data)       # 全为偶数
assert any(x > 5 for x in data)            # 存在 >5 的

print("12. 综合练习 OK")
print("\n全部通过! ✓")
