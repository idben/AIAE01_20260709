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

# 刪除
s3.remove(4)
print("s3", s3)
# s3.remove(4) # 刪除不存在的元素, 會丟出錯誤
s3.discard(5)
s3.discard(155) # 刪除不存在的元素, 不會錯誤, 相對安全
print("s3", s3)

# 集合運算
users_a = {"Ben", "Amy", "Ken"}
users_b = {"Ken", "Ivy", "Tom"}

common = users_a & users_b
only_a = users_a - users_b
all = users_a | users_b
diff = users_a ^ users_b
print("common", common)
print("only_a", only_a)
print("all", all)
print("diff", diff)

# 集合運算使用情境
old_users = [
    {"id": 1, "name": "Ben"},
    {"id": 2, "name": "Sean"},
    {"id": 3, "name": "Ann"},
]
new_users = [
    {"id": 2, "name": "Sean"},
    {"id": 3, "name": "Ann"},
    {"id": 4, "name": "May"},
]

# 一般建立方法
old_ids = set()
for user in old_users:
    old_ids.add(user["id"])
print("old_ids", old_ids)

# set 推導式
new_ids = {user["id"] for user in new_users}
print("new_ids", new_ids)

same_ids = old_ids & new_ids # 交集
print("same_ids", same_ids)
added_ids = new_ids - old_ids # 差集, 新減舊 ,新增的使用者
print("added_ids", added_ids)
removed_ids = old_ids - new_ids # 差集, 舊減新 ,被刪除的使用者
print("removed_ids", removed_ids)
all_ids = old_ids | new_ids
print("all_ids", all_ids)

# 一般取得完整資料方式
new_user_dict = {}
# {
#     2: {"id": 2, "name": "Sean"},
#     3: {"id": 3, "name": "Ann"},
#     4: {"id": 4, "name": "May"},
# }

for user in new_users:
    new_user_dict[user["id"]] = user
print(new_user_dict)

added_users = []
for id in added_ids:
    added_users.append(new_user_dict[id])

print(added_users)