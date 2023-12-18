from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

import DatabaseFunctions as dbf

class HospitalGui(QMainWindow):
    def __init__(self,):
        super(HospitalGui,self).__init__()
        uic.loadUi("HMS_UI.ui",self)
        self.show()

        self.AddRecordButton.clicked.connect(self.AddRecord)

        labels,records = dbf.ListDoctors()
        self.LoadTable(labels,records)
        

    def LoadTable(self,labels,records):
        self.Table.setRowCount(len(records))
        self.Table.setColumnCount(len(labels))

        self.Table.setHorizontalHeaderLabels(labels)
        for rowindex,row in enumerate(records):
            for columnindex,element in enumerate(row):
                self.Table.setItem(rowindex,columnindex,QTableWidgetItem(str(element)))

      


    def AddRecord(self):
        rowcount = self.Table.rowCount()
        self.Table.insertRow(rowcount)

app = QApplication([])
window = HospitalGui()

app.exec()