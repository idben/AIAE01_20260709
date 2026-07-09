import copy

# 串列的複製現象
# 等號是指向，不是複製
list_a = [1,2,3]
list_b = list_a
list_c = list_a.copy()  # 淺拷貝

list_b[0] = 999
print(list_a)
print(list_b)
print(list_c)
print("-"*30)

list1 = [[1,2], [3,4]] # 二維串列
list2 = list1.copy() # 淺拷貝只對第一層有用
list3 = copy.deepcopy(list1) # 要在程式碼最前面載入 copy, 才能使用 deepcopy
print(f"取出 list2 的索引0 的索引0 : {list2[0][0]}")
list2[0][0] = 999
print(list1)
print(list2)
print(list3)