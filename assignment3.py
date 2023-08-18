# Multi-Dimention List(nested list)

customer = ["Joseph", "Nyahururu", ["jose@gmail.com", "0712345678"], ["Vegetables", "Flowers", "Fruits"]]

# 1. Access Joseph's phone
phone = customer[2][1]
print(phone)

# 2. Access Vegetables and Flowers Only
products = customer[3][0:2]
print(products)
