from users import User, Admin
from stock import StockItem, Inventory
from money import Money

from datetime import datetime


class Purchase():
    """Handles purchases(and receipts)"""
    purchases = {} # for later access/reference (to Purchase attributes)
    receipt_ref_no = 0 #not sure if this is neccessary, so itll remain (till i decide)
    def __init__(self, *items):
        self.date = str(datetime.now()) #need to limit to seconds
        self.items = items
        for user, v in User.user_accounts.items():
            # This for loop checks for whichever user is currently loged in and
            # makes that user the issuer of the receipt 
            v = v #put this here because my IDE was like"mm unused variable v?" 😅
            if User.users[user].logedin:
                self.issuer = user
      
        self.purchase_items = {} #contains purchased item's name:price*amnt purchased
       
        for item in self.items:
            for item, amnt in item:
                if item in Inventory.inventoryList:
                    self.purchase_items[item] = Inventory.inventory[item].ItemSellPrice * amnt
                    Inventory.inventory[item].updatestock(amnt)
                    # print(f"{item} rem {Inventory.inventory[item].amount} in Inv")
                    
                else:
                    # real case scenerio the below statement
                    # shouldnt be needed as ill try to make sure
                    # appropiate info gets through, regardless its a gui
                    # not terminal based so either way kind of useless
                    # or not, anyhow its for debugging purposes😅.
                    print(f"{item} not in inventory")
                    pass
        
        self.total = 0
       
        for k,v in self.purchase_items.items():
            self.total += v
            k = k
        Money.update(Money,-self.total, "Item Purchase")
        self.purchases[self.date] = self
        

        

    def preview(self, *items):
        self.receipt_preview = {}
       
        for item in items:
            if item in Inventory.inventoryList:
                self.receipt_preview[item] = Inventory.inventory[item].ItemSellPrice
                
            else:
                # real case scenerio the below statement
                # shouldnt be needed as ill try to make sure
                # appropiate info gets through, regardless its a gui
                # not terminal based so either way kind of useless
                # or not, anyhow its for debugging purposes😅.
                print(f"{item} not in inventory")
                pass
        
        self.receipt_preview_total = 0
       
        for k,v in self.receipt_preview.items():
            self.receipt_preview_total += v
            k = k

        return self.receipt_preview, self.receipt_preview_total

   