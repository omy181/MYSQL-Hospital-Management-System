from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

import DatabaseFunctions as dbf

class HospitalGui(QMainWindow):
          
    def __init__(self):
        super(HospitalGui,self).__init__()
        uic.loadUi("HMS_UI.ui",self)
        self.show()

        self.InitializePanelSelector()
        
        self.AddRecordButton.clicked.connect(self.AddRecord)
        self.Table.cellChanged.connect(self.SaveCell)
        self.Table.cellClicked.connect(self.SelectRow)
        self.DeleteSelectedRow.clicked.connect(self.DeleteRow)
        self.PanelSelector.activated.connect(self.PanelChanged)


    def InitializePanelSelector(self):
        tables = ["Doctor","Patient","Appointment","Medical_Prescription"]
        for table in tables:
            self.PanelSelector.addItem(table)

        self.PanelChanged()

    def PanelChanged(self):
        self.CurrentPanel = self.PanelSelector.currentText()
        self.RefreshTable()

    def RefreshTable(self):
        self.labels,self.records = dbf.ListTable(self.CurrentPanel)
        self.LoadTable(self.labels,self.records)   
        self.tableCount.setText(f"Record Count: {dbf.GetRecordCount(self.CurrentPanel)}")
        self.SelectedID = -1
        self.DeleteRow()

    def LoadTable(self,labels,records):
        self.Table.setRowCount(len(records))
        self.Table.setColumnCount(len(labels))

        self.Table.setHorizontalHeaderLabels(labels)
        for rowindex,row in enumerate(records):
            for columnindex,element in enumerate(row):
                self.Table.setItem(rowindex,columnindex,QTableWidgetItem(str(element)))

    def SelectRow(self,row,column):
        self.SelectedID = self.records[row][0]
        self.DeleteSelectedRow.setText(f"Delete ID {self.SelectedID}")
        self.DeleteSelectedRow.setEnabled(True)

    def AddRecord(self):

        dbf.AddNewRecord(self.CurrentPanel)

        self.RefreshTable()

    def DeleteRow(self):
        if self.SelectedID != -1:
            dbf.RemoveRecord(self.CurrentPanel,self.SelectedID)
            self.RefreshTable()
        else:
            self.DeleteSelectedRow.setEnabled(False)
            self.DeleteSelectedRow.setText(f"Delete Selected Row")

    def SaveCell(self,row,column):
        item = self.Table.item(row,column)
        itemtoprint = ""
        if item != None:
            itemtoprint = item.text()

        if dbf.UpdateRecord(self.CurrentPanel,int(self.records[row][0]),self.labels[column],itemtoprint) is False:
            self.RefreshTable()
            self.MessageBox("Can't modify cell value","Error")

    def MessageBox(self,message,title):
        dialog = QMessageBox()   
        dialog.setText(message)
        dialog.setWindowTitle(title) 
        dialog.setIcon(QMessageBox.Warning)
        dialog.exec_()

app = QApplication([])
window = HospitalGui()

app.exec()