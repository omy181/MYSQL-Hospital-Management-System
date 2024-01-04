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
        self.Refresh.clicked.connect(self.RefreshTable)

        # optional buttons
        self.OrderByDate.clicked.connect(self.OrderByDateTable)


    def InitializePanelSelector(self):
        tables = ["Doctor","Patient","Appointment","Medical_Prescription"]
        for table in tables:
            self.PanelSelector.addItem(table)

        self.PanelChanged()

    def PanelChanged(self):
        self.CurrentPanel = self.PanelSelector.currentText()
        self.RefreshTable()

    def RefreshTable(self,orderby_type=-1):
        self.labels,self.records = dbf.ListTable(self.CurrentPanel,orderby_type)
        self.LoadTable(self.labels,self.records)   

        # button activations
        self.OrderByDate.setEnabled(False)
        earliestapp = ""
        latestapp = ""
        mostappdoc = ""
        match self.CurrentPanel:
            case "Appointment":
                self.OrderByDate.setEnabled(True)
                id,date = dbf.GetMinMaxRecord(self.CurrentPanel,"min")
                earliestapp = f"Earliest Appointment: ID:{id} Date:{date}"
                id,date = dbf.GetMinMaxRecord(self.CurrentPanel,"max")
                latestapp += f"Latest Appointment: ID:{id} Date:{date}"
            case "Patient":
                self.OrderByDate.setEnabled(True)
                id,date = dbf.GetOldestYoungestPatientAge("min")
                earliestapp = f"Oldest Patient: ID:{id} Age:{date}"
                id,date = dbf.GetOldestYoungestPatientAge("max")
                latestapp += f"Youngest Patient: ID:{id} Age:{date}"
                age = dbf.GetAveragePatientAge()
                mostappdoc = f"Average Patient Age: {age}"
            case "Doctor":
                id,count = dbf.GetMostAppointedDoctor()
                earliestapp = f"Most Appointed Doctor: ID:{id} Count:{count}"

        self.tableCount.setText(f"Record Count: {dbf.GetRecordCount(self.CurrentPanel)}")
        self.earliestapp.setText(earliestapp)
        self.latestapp.setText(latestapp)
        self.mostappdoc.setText(mostappdoc) 
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
            try:
                dbf.RemoveRecord(self.CurrentPanel,self.SelectedID)
            except:
                self.MessageBox("This Record is used as a Foreign Key","Error")
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

    def OrderByDateTable(self):
        self.RefreshTable(dbf.TableValues[self.CurrentPanel]["Date"])

app = QApplication([])
window = HospitalGui()

app.exec()