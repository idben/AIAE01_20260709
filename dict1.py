# tuple 的最後, 做為字典的 key
d1 = {"id": 1, "color": "black", "size": "M", "price": 380}
d2 = {("black", "M"): 380}
print(d2)

prices = {
    ("apple", "small"): 10,
    ("apple", "large"): 18,
    ("banana", "small"): 8,
}
f = "banana"
s = "small"
print(prices[f, s])
print("-"*30)

# 字典的基本表現方式
# 大括號字面值
d3 = {"k1": 1, "k2": 2}
d4 = dict(k1=1, k2=2) # 建構子
print("d3", d3)
print("d4", d4)

pairs = [("k1", 1), ("k2", 2)]
d5 = dict(pairs)
print("d5", d5)

keys = ["k1", "k2"]
values = [1, 2]
print(list(zip(keys, values)))
d6 = dict(zip(keys, values))
print("d6", d6)