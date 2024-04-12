"""Practice writing Twitter profile Class"""


class Profile:


    username: str 
    private: bool
    

    def __init__(self, username_input: str):
        """Create new Profile"""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """If Profile is not Private Print Message"""
        if self.private is not True:
            print(msg)
    

user1: Profile = Profile("110 rulz")
user1.private = False
user1.tweet("OOP is cool!")










