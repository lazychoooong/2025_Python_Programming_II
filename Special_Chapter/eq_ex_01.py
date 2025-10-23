class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, User):
            return self.name == other.name
        return False

user1 = User("Kim")
user2 = User("Lee")
user3 = User("Park")
user5 = User("Kim")

users = [user1, user2]

print(user1 in users)
print(user2 in users)
print(user3 in users)
print(user5 in users)