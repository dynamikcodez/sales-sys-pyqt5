import datetime

class Inventory():
    """contains a dict of all Sock items so their StockItem (
        Class) attributes can be accessed and a list of all SI"""
    inventory = {}
    inventoryList = []

    def __init__(self):
            pass

class StockItem():
    """Handles stock items"""
    def __init__(self, name,exp, sell_price, amount,description = """Null"""):
                
                if name not in Inventory.inventoryList:
                        pass
                else:
                        print("Item already in Inventory") 
                        return                  

                self.ItemName = name
                self.description = description
                self.ItemBB = exp
                self.amount = amount
                self.ItemSellPrice = sell_price
                self.dateadded = datetime.datetime.now()
                # sellprice, buyprice = ?,?
                print(f"{self.ItemName} Item added")

                Inventory.inventory[self.ItemName] = self # for later/easy access  
                Inventory.inventoryList.append(self.ItemName)

    def updatestock(self, amnt):
        self.amount -= amnt
        return self.amount

    def delete_stock_item(self):
        pass

