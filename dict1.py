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