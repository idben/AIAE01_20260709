# sort
list1 = [3,1,10,2]
list1.sort()
list1.sort(reverse=True)
print(list1)

# sort key
list2 = ["cc", "b", "aaa"]
list2.sort()
list2.sort(key=len)
print(list2)

# sort key lambda
# lambda 匿名函式
# 公式:  lambda 參數名: 公式
words = ["banana", "apple", "cherry"]
words.sort(key=lambda word: word[2])
print(words)

# sort key lambda + 真實資料
datas = [
    {"id": 1, "name": "Ben", "age": 38},
    {"id": 2, "name": "May", "age": 18},
    {"id": 3, "name": "John", "age": 28}
]
datas.sort(key=lambda data: data["age"], reverse=True)
print(datas)