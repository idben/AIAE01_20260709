# tuple 的基本表現方式
point = (10, 20)
print(f"座標是: {point}")
print(f"X 座標是: {point[0]}")

point2 = 30, 40 # taple packing, 元祖打包, 重點是逗號
print(type(point2).__name__)

# 空 tuple
empty = ()
print(len(empty))
print(type(empty))

# 單一元素，要多一個半形逗點才能形成單一元素 tuple
a = [3]
b = (3)
c = (3,)
print(a, type(a))
print(b, type(b))
print(c, type(c))

# tuple 的內容可以混合型別
t1 = (1, 1, "a", True, None, [1, 2, 3], (1, 2), {"id": 3, "name": "Ben"})
print(t1, type(t1))

# tuple 的不可變
print(t1[1])
# t1[1] = 2   # 會出錯, 不支援重新指定 tuple 內容
t1[5][0] = 99
print(t1, type(t1))
print("-"*30)

# 基本解包
t2 = (10, 20, 30)
# a = t2[0]
# b = t2[1]
# c = t2[2]
a, b, c = t2
print(f"a 是 {a}")
print(f"b 是 {b}")
print(f"c 是 {c}")

# 星號解包
a, *others = t2
print(f"a 是 {a}")
print(f"others 是 {others}")
print("-"*30)

# 修改 tuple 的內容 = 以新 tuple 覆蓋
t3 = (10, 20, 30, 40)
index = 1
new_value = 999
# tuple 相加 = 合併
t3 = t3[:index] + (new_value,) + t3[index+1:]
print(t3)
