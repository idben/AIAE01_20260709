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