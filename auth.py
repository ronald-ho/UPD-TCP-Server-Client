ACTIVE_USERS    = "active_users.txt"
CREDENTIALS     = "credentials.txt"

class Authenticate():

    def __init__(self):
        self.users = self.readCredentials()

    def readCredentials(self):
        userDict = {}

        with open(CREDENTIALS, "r") as auth:
            credentials = auth.readlines()
            for line in credentials:
                userDict[line.split[0]] = line.split[1]

        return userDict

    def passwordIsValid(self, password):
        if len(password) == 0 or not password.isalnum() or not password.isprintable():
            return False

        return True

    def usernameExist(self, username):
        return username in self.users
    
    def authentication(self, username, password):
        if self.usernameExist(username):
            return self.users[username] == password
                
    def login(self, username, password):
        if self.authenticate(username, password):
            with open(ACTIVE_USERS, "a") as active:
                active.write(f"{username}\n")

    def logout(self, username):
        # If the user is logged in, remove the user from the active users file  
        with open(ACTIVE_USERS, "r+") as active:
            users = active.readlines()
            for user in users:
                if user.strip() == username:
                    users.remove(user)

    def register(self, username, password):
        if self.usernameExist(username):
            return False

        if self.passwordIsValid(password):
            with open(CREDENTIALS, "a") as auth:
                auth.write(f"{username} {password}\n")
            return True

        return False

    def getActiveUsers(self):
        with open(ACTIVE_USERS, "r") as active:
            return active.readlines()