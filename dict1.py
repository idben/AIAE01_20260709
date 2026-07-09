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

# 更新多筆
# 注意 .update() 有兩種使用方式, 一個是傳入一個 dict,
# 一個是使用建構子方式更新
d7 = {"k3": 3, "k4": 4}
d6.update(d7)
d6.update(k5=5, k6=6, k7=7)
print("d6", d6)
print("-"*30)

# 刪除
del d6["k4"]
print("d6", d6)
# del d6["k14"]     # 刪除不存在的 key 會出錯
v_del = d6.pop("k5")
print("d6", d6)
print("v_del", v_del)
# d6.pop("k15")       # 刪除不存在的 key 會出錯
v_del2 = d6.popitem() # .popitem() 刪除最後插入的一筆
print("d6", d6)
print("v_del2", v_del2)

d6.clear()
print("d6", d6)
print("-"*30)

# 走訪(遍歷)
d = {"name": "Ben", "age": 18, "city": "Taipei"}

for k, v in d.items():
    print(k, v)
# keys() / values()
print(d.keys())
print(d.values())