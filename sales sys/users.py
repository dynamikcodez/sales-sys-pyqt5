class User():
    """Main user class"""
    user_accounts = {} #stores all usernames and passwords
    # user_accounts["dynamik"] = "dynamik" #test user
    users = {} #for later access/reference (to user attributes) 
    def __init__(self,username, password, type_= "WORKER"):
        self.username = username
        self.password = password
        self.UserType = type_
        self.user_accounts[self.username] = self.password
        self.logedin = False
        self.users[self.username] = self

    def authenticate(self, entusername, entpassword):
        """Authenticates Log in (attempt(s))"""
        self.EnteredUsername = entusername
        self.EnteredPassword = entpassword

        if self.EnteredUsername in self.user_accounts:
            if self.user_accounts[self.EnteredUsername] == self.EnteredPassword:
                return True
        else:
            return False

    def login(self):
        self.logedin = True 
        return self.logedin

    def logout(self):
        self.logedin = False
        return self.logedin

    def loginstatus(self):
        return self.logedin
    
    def user_type(self):
        """Display's user's type(WORKER or ADMIN) """
        UserType = (f"{(self.UserType)}")
        return UserType


class Admin(User):
    def __init__(self,username, password, type_= "ADMIN"):
        super().__init__(username, password, type_)

class Worker(User):
    def __init__(self,username, password, type_ = "WORKER"):
        super().__init__(username, password, type_)

