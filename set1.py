# set 的基本表現方式
s1 = {1, 2, 3}
print("s1", s1)
# print(s1[0]) # 因為 set 沒有順序性, 所以不像 list 可以中括號加索引來取值

s2 = set() # 空 set
print(len(s2)) # 長度
print(type(s2)) 

# 放 list 進去轉 set，去除重複常用
list1 = [1, 2, 2, 3]
s3 = set(list1)
print("s3", s3)

# 新增(單一元素)
s3.add(4)
s3.add(5)
# s3.add([6, 7]) # add 只能夠放可以 hash 的內容, list/dict 無法

# update(更新一組 list)
s3.update([6, 7, 7])
print("s3", s3)