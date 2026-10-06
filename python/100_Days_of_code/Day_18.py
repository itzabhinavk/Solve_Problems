# Day 18 - 100 Days of Code Challenge





def get():
    print(" this is second function in ")

users = [
    {"name": "Alice", "is_active": True},
    {"name": "varsha", "is_active": False},
    {"name": "Charlie", "is_active": True}
]
index = int(input("Enter the index of the user: "))
user = users[index]
print(user)
if user.is_active:
    print("user is active")

