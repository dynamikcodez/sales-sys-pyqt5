import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

import stock 

class MainPurchaseWin(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Sales system"      
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0,0,1366,786)
        # Making scroll Area for purchases
        self.scrollArea = qtw.QScrollArea(self)
        self.scrollArea.setMinimumSize(500,700)
        # self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = qtw.QWidget()#layout for scrollArea(where elements get added for display)
        self.scrollAreaWidgetContents.setMinimumSize(500,800)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents) #setting layout

        # creating search box
        self.search_entry = qtw.QLineEdit(self)
        self.search_entry.setMaximumHeight(25)
        self.search_entry.setMinimumWidth(200)
        self.search_entry.move(1000,0) 
        self.search_btn = qtw.QPushButton("Search", self)
        self.search_btn.clicked.connect(self.search)
        self.search_btn.setFixedSize(80,20)
        self.search_btn.move(1200, 3)
        self.clearbtn = qtw.QPushButton("X", self)
        self.clearbtn.setMaximumSize(20,25)
        self.clearbtn.move(1180,0)
        self.clearbtn.clicked.connect(self.clearsearch)

        # Some logic(al(Variable declarations))
        self.searched = self.search_entry.text()




        # setting mainlayout
        self.show()

        # Program Logic
        stock.db_handeling()
        BB = str((2021, 12, 12))
        
        stock.AddToStock("Sprite",100,BB,32,'Sugary water')
        stock.AddToStock("Fanta", 120, BB , 24,"")
    
    def search(self):
        self.search_results = qtw.QListWidget(self)
        self.searched = self.search_entry.text()
        item_list = stock.search(self.searched)
        if item_list:
            for x in item_list:
                if self.searched in item_list:
                    x = qtw.QListWidgetItem(str(x))
                    self.search_results.addItem(x)
        self.search_results.move(1000,25)
        self.search_results.setMinimumHeight(50)
        self.search_results.show()

    def clearsearch(self):
        self.search_results.deleteLater()
            
    
        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainPurchaseWin()
    sys.exit(app.exec_())