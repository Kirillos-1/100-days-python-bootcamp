class User:
    def __init__(self, user_id: str, username: str) -> None:
        print("New user being created...")
        
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    
    def follow(self, user):
        user.followers += 1
        user.following += 1
    
    
user_1 = User("001", "angela")
user_2 = User("002", "Jack")

print(user_1.id)
print(user_1.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_2.following)

print(user_1.following)
print(user_2.followers)