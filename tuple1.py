# tuple 的基本表現方式
point = (10, 20)
print(f"座標是: {point}")
print(f"X 座標是: {point[0]}")

point2 = 30, 40 # taple packing, 元祖打包, 重點是逗號
print(type(point2).__name__)