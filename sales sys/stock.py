import datetime, sqlite3, json




    # def updatestock(self, amnt):
    #     self.amount -= amnt
    #     return self.amount

    # def delete_stock_item(self):
    #     pass
  
    # def pricechange(self, newprice):
    #     date = str(datetime.datetime.now())
    #     self.price = newprice
    #     self.pricehistory[date] = self.price
    #     return self.pricehistory, self.price 
   
    # def checkexpiration(self):
    #     daysToBB = (self.ItemBB - datetime.datetime.today()).days
       
    #     if daysToBB <= 14:
    #         print("Item will expire in", daysToBB, "days")
    #     return daysToBB


# _________________________________DATABASE___________________________#
conn = sqlite3.connect(':memory:')
c = conn.cursor()
def db_handeling():

    
    c.execute("""CREATE TABLE IF NOT EXISTS STOCKITEMS (
        ItemName text,
        ItemPrice integer,
        ItemProfit,
        ItemBB BLOB,
        ItemAmount integer,
        ItemDescription text,
        DateAdded BLOB,
        PriceHistory BLOB
    ) """)
    print("DB created")

def AddToStock(Name, Price, BB, Amnt,Desc="Nill"):
    """BB should be a tuple in the format (year, month, day) regardless
        of wether theres a specific day or not(just put 1)"""
    Moment = datetime.datetime.now()
    Moment = str(Moment)[:16]
    ItemName = Name
    ItemPrice = Price
    ItemProfit = ItemPrice*0.1
    ItemAmount = Amnt
    ItemBB = BB.strip("( )")
    ItemDescription = Desc
    PriceHistory = {}
    PriceHistory[Moment] = ItemPrice
    JPriceHistory = json.dumps(PriceHistory)
    DateAdded = str(Moment)
    
    stockattr = [(ItemName, 
                ItemPrice, 
                ItemProfit,
                ItemBB,
                ItemAmount,
                ItemDescription, 
                DateAdded,
                JPriceHistory)]
    c.executemany("""INSERT INTO STOCKITEMS VALUES(?,?,?,?,?,?,?,?)""", stockattr)


def search(query):
    c.execute("SELECT ItemName FROM STOCKITEMS")
    itemNames = c.fetchall()
    item_list = []
    for names in itemNames:
        item_list.append(names[0])
        #Items are stored as tuples in sqlite3, hence the indexing
    for item in item_list:
        if query in str(item).lower():
            print(query, "in db ", item)
            return item_list



# i dont think i need to handle money at hand, just monitor money
# and profit made for each day(ill need to a add a times_price variable, 
# that stores the price of an item at any given time).