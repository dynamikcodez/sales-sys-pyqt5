from users import User, Admin
from stock import StockItem, Inventory
from purchase import Purchase
from money import Money

from datetime import datetime  




# (("fanta", 2), ("sprite", 3))


# ________________________program logic_________________________#

fanta = StockItem("fanta",0, 120, 248, "Orange juice")
fanta = StockItem("fanta2",0, 1220, 224, "2Orange juice")

sprite = StockItem("sprite",0, 120, 24, "sweet water😅")
print(Purchase.preview(Purchase, "fanta", "sprite", "Bobo"))

r = Purchase((("fanta", 18), ("sprite", 1)))
print(r.total)
# r2 = Purchase.preview(Purchase,"dud","fanta", "sprite")
# r3 = Purchase.preview(Purchase,"dud","fanta","fanta", "sprite")

# Money = Money(2300)

# Money.update(1200, "Used to restock")

# print(Money.money_history)
# Money.update(-1200, "given to manager")
# print(Money.money_history)


ADMIN = User("ADMIN", "ADMIN")
ADMIN2 = User("ADMIN2", "ADMIN")
ADMIN3 = User("ADMIN3", "ADMIN")

def login(username, password):
    username = username
    password = password
    User.authenticate(User, username, password)

# print(login("ADMIN2", "ADMIN"))

def login1():
    """First logs out previous users then logs in new user """
    for user, v in User.user_accounts.items():
        if User.users[user].logedin:
            v = v #put this here because my IDE was like"mm unused variable v?" 😅
        
            User.users[user].logout()
            
    username = input("Enter your username: ")
    password = input("Enter corresponding password: ")

    if User.authenticate(User, username, password):
        print("Log in success")
        User.users[username].login()
        print(User.users[username].login())
        print(User.users[username].UserType)
        
    else:
        print("Log in False")



#The attributes of StockItem instances can be accessed by
#using their string name in the Inventory.inventory list
#Eg. x = StockItem("x", 0, 0, "0"), x can be accessed later 
#as Inventory.inventory["x"](. whatever(for attribute reference)) 