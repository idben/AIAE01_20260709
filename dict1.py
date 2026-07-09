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
print("-"*30)

# 取值
print("d6 的 k1 是", d6["k1"])
if "k3" in d6:
    print("d6 的 k3 是", d6["k3"])    # 用 [] 取字典內容時, key 不存在, 會丟出錯誤

print("d6 的 k3 是", d6.get("k3"))    # 使用 .get() 取用字典內容，不存在時會回傳 None
print("d6 的 k3 是", d6.get("k3", 0)) # 使用 .get() 取用字典內容，可以設定不存在時回傳的值，也叫預設值

# try-except 會補獲執行階段的錯誤
try:
    print("d6 的 k3 是", d6["k3"])
    a5 = d6["k3"]
except:
    print("剛剛有錯誤產生")
    a5 = None

print("a5", a5)
v1 = d6.setdefault("k4", 666)
print("v1", v1)