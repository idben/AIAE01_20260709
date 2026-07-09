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
print("-"*30)

# sorted 不會改變原始對象, 會回傳新內容
list1 = [3,1,10,2]
print(sorted(list1))

list2 = ["cc", "b", "aaa"]
print(f"原始串列: {list2}")
print(f"排序後的結果: {sorted(list2, key=len)}")

datas = [
    {"id": 1, "name": "Ben", "age": 38},
    {"id": 2, "name": "May", "age": 18},
    {"id": 3, "name": "John", "age": 28}
]
print(f"原始資料: {datas}")
print(f"排序後的資料: {sorted(datas, key=lambda d: d["age"])}")
print("-"*30)

# sorted 實例 2
# 在不改變原始名單的狀況下，取前三名
scores = [
    {"id": 1, "name": "Joe", "score": 85},
    {"id": 2, "name": "Allice", "score": 92},
    {"id": 3, "name": "Ken", "score": 75},
    {"id": 4, "name": "Ben", "score": 90},
    {"id": 5, "name": "Karen", "score": 88},
]
print(sorted(scores, key=lambda st: st["score"], reverse=True)[0:3])


# 方法 2
# 搭配複製串列﹑反轉串列和切片取前三名
scores_new = scores.copy()
scores_new.sort(key=lambda st: st["score"])
scores_new.reverse()
print(scores_new[0:3])