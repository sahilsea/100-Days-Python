class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "angela"

# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"

# user_3 = User()
# user_3.id = "003"
# user_3.username = "Sahil"

# user_4 = User()
# user_4.id = "002"f
# user_4.username = "Rahul"

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
user_3 = User("003", "Sahil")
user_4 = User("004", "Rahul")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)