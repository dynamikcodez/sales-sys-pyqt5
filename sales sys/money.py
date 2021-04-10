from datetime import datetime

class Money():
    money_history = {} #{date : description, money_balance}
    Money_balance = 0
    def __init__(self, amount):
        # self.amount = amount
        self.Money_balance = amount
        pass

    def update(self, amount, description):
        """Adds/subtracts to/from Money_balance"""
        date = str(datetime.now())
        if self.Money_balance - amount >= 0:
            self.Money_balance -= amount
            self.money_history[date] = description, self.Money_balance
            return self.Money_balance
        else:
            # print("false")
            return False
