# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cpuSchedulerGUI5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import Overlord
import random
import math
import Algorithms
import threading

"""class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        self.mastercontrol()"""

class Ui_CPU_Scheduler(object):
    def setupUi(self, CPU_Scheduler):
        self.throughputresults = {}
        self.turnaroundresults = {}
        self.waitresults = {}
        self.responseresults = {}
        self.files = []
        self.usedflag = ""
        CPU_Scheduler.setObjectName("CPU_Scheduler")
        CPU_Scheduler.resize(419, 309)
        self.gridLayout = QtWidgets.QGridLayout(CPU_Scheduler)
        self.gridLayout.setObjectName("gridLayout")
        self.widgetOutput = QtWidgets.QWidget(CPU_Scheduler)
        self.widgetOutput.setMinimumSize(QtCore.QSize(401, 291))
        self.widgetOutput.setObjectName("widgetOutput")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetOutput)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.processInput = QtWidgets.QTextEdit(self.widgetOutput)
        self.processInput.setMinimumSize(QtCore.QSize(131, 31))
        self.processInput.setMaximumSize(QtCore.QSize(131, 31))
        self.processInput.setObjectName("processInput")
        self.gridLayout_2.addWidget(self.processInput, 0, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.widgetOutput)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 2, 6, 1)
        self.run_btn = QtWidgets.QPushButton(self.widgetOutput)
        self.run_btn.setMinimumSize(QtCore.QSize(131, 31))
        self.run_btn.setObjectName("run_btn")
        self.gridLayout_2.addWidget(self.run_btn, 4, 0, 1, 2)
        self.writeData_btn = QtWidgets.QPushButton(self.widgetOutput)
        self.writeData_btn.setMinimumSize(QtCore.QSize(131, 31))
        self.writeData_btn.setObjectName("writeData_btn")
        self.gridLayout_2.addWidget(self.writeData_btn, 5, 0, 1, 2)
        self.coreCount = QtWidgets.QSpinBox(self.widgetOutput)
        self.coreCount.setMinimum(0)
        self.coreCount.setMaximum(99)
        self.coreCount.setProperty("value", 4)
        self.coreCount.setObjectName("coreCount")
        self.gridLayout_2.addWidget(self.coreCount, 2, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widgetOutput)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 2)
        self.coreCount_lbl = QtWidgets.QLabel(self.widgetOutput)
        self.coreCount_lbl.setObjectName("coreCount_lbl")
        self.gridLayout_2.addWidget(self.coreCount_lbl, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.widgetOutput)
        self.tabWidget.setMaximumSize(QtCore.QSize(131, 81))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.algorithm1tab = QtWidgets.QWidget()
        self.algorithm1tab.setObjectName("algorithm1tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.algorithm1tab)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.algorithm1 = QtWidgets.QComboBox(self.algorithm1tab)
        self.algorithm1.setObjectName("algorithm1")
        self.algorithm1.addItem("")
        self.algorithm1.addItem("")
        self.algorithm1.addItem("")
        self.algorithm1.addItem("")
        self.algorithm1.addItem("")
        self.algorithm1.addItem("")
        self.verticalLayout_7.addWidget(self.algorithm1)
        self.RRTimeQ1 = QtWidgets.QSpinBox(self.algorithm1tab)
        self.RRTimeQ1.setMinimum(1)
        self.RRTimeQ1.setObjectName("RRTimeQ1")
        self.verticalLayout_7.addWidget(self.RRTimeQ1)
        self.tabWidget.addTab(self.algorithm1tab, "")
        self.algorithm2tab = QtWidgets.QWidget()
        self.algorithm2tab.setObjectName("algorithm2tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.algorithm2tab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.algorithm2 = QtWidgets.QComboBox(self.algorithm2tab)
        self.algorithm2.setObjectName("algorithm2")
        self.algorithm2.addItem("")
        self.algorithm2.addItem("")
        self.algorithm2.addItem("")
        self.algorithm2.addItem("")
        self.algorithm2.addItem("")
        self.algorithm2.addItem("")
        self.verticalLayout_8.addWidget(self.algorithm2)
        self.RRTimeQ2 = QtWidgets.QSpinBox(self.algorithm2tab)
        self.RRTimeQ2.setMinimum(1)
        self.RRTimeQ2.setObjectName("RRTimeQ2")
        self.verticalLayout_8.addWidget(self.RRTimeQ2)
        self.tabWidget.addTab(self.algorithm2tab, "")
        self.algorithm3tab = QtWidgets.QWidget()
        self.algorithm3tab.setObjectName("algorithm3tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.algorithm3tab)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.algorithm3 = QtWidgets.QComboBox(self.algorithm3tab)
        self.algorithm3.setObjectName("algorithm3")
        self.algorithm3.addItem("")
        self.algorithm3.addItem("")
        self.algorithm3.addItem("")
        self.algorithm3.addItem("")
        self.algorithm3.addItem("")
        self.algorithm3.addItem("")
        self.verticalLayout_6.addWidget(self.algorithm3)
        self.RRTimeQ3 = QtWidgets.QSpinBox(self.algorithm3tab)
        self.RRTimeQ3.setMinimum(1)
        self.RRTimeQ3.setObjectName("RRTimeQ3")
        self.verticalLayout_6.addWidget(self.RRTimeQ3)
        self.tabWidget.addTab(self.algorithm3tab, "")
        self.algorithm4tab = QtWidgets.QWidget()
        self.algorithm4tab.setObjectName("algorithm4tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.algorithm4tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.algorithm4 = QtWidgets.QComboBox(self.algorithm4tab)
        self.algorithm4.setObjectName("algorithm4")
        self.algorithm4.addItem("")
        self.algorithm4.addItem("")
        self.algorithm4.addItem("")
        self.algorithm4.addItem("")
        self.algorithm4.addItem("")
        self.algorithm4.addItem("")
        self.verticalLayout_5.addWidget(self.algorithm4)
        self.RRTimeQ4 = QtWidgets.QSpinBox(self.algorithm4tab)
        self.RRTimeQ4.setMinimum(1)
        self.RRTimeQ4.setObjectName("RRTimeQ4")
        self.verticalLayout_5.addWidget(self.RRTimeQ4)
        self.tabWidget.addTab(self.algorithm4tab, "")
        self.algorithm5tab = QtWidgets.QWidget()
        self.algorithm5tab.setObjectName("algorithm5tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.algorithm5tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.algorithm5 = QtWidgets.QComboBox(self.algorithm5tab)
        self.algorithm5.setObjectName("algorithm5")
        self.algorithm5.addItem("")
        self.algorithm5.addItem("")
        self.algorithm5.addItem("")
        self.algorithm5.addItem("")
        self.algorithm5.addItem("")
        self.algorithm5.addItem("")
        self.verticalLayout_4.addWidget(self.algorithm5)
        self.RRTimeQ5 = QtWidgets.QSpinBox(self.algorithm5tab)
        self.RRTimeQ5.setMinimum(1)
        self.RRTimeQ5.setObjectName("RRTimeQ5")
        self.verticalLayout_4.addWidget(self.RRTimeQ5)
        self.tabWidget.addTab(self.algorithm5tab, "")
        self.algorithm6tab = QtWidgets.QWidget()
        self.algorithm6tab.setObjectName("algorithm6tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.algorithm6tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.algorithm6 = QtWidgets.QComboBox(self.algorithm6tab)
        self.algorithm6.setObjectName("algorithm6")
        self.algorithm6.addItem("")
        self.algorithm6.addItem("")
        self.algorithm6.addItem("")
        self.algorithm6.addItem("")
        self.algorithm6.addItem("")
        self.algorithm6.addItem("")
        self.verticalLayout_3.addWidget(self.algorithm6)
        self.RRTimeQ6 = QtWidgets.QSpinBox(self.algorithm6tab)
        self.RRTimeQ6.setMinimum(1)
        self.RRTimeQ6.setObjectName("RRTimeQ6")
        self.verticalLayout_3.addWidget(self.RRTimeQ6)
        self.tabWidget.addTab(self.algorithm6tab, "")
        self.algorithm7tab = QtWidgets.QWidget()
        self.algorithm7tab.setObjectName("algorithm7tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.algorithm7tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.algorithm7 = QtWidgets.QComboBox(self.algorithm7tab)
        self.algorithm7.setObjectName("algorithm7")
        self.algorithm7.addItem("")
        self.algorithm7.addItem("")
        self.algorithm7.addItem("")
        self.algorithm7.addItem("")
        self.algorithm7.addItem("")
        self.algorithm7.addItem("")
        self.verticalLayout_2.addWidget(self.algorithm7)
        self.RRTimeQ7 = QtWidgets.QSpinBox(self.algorithm7tab)
        self.RRTimeQ7.setMinimum(1)
        self.RRTimeQ7.setObjectName("RRTimeQ7")
        self.verticalLayout_2.addWidget(self.RRTimeQ7)
        self.tabWidget.addTab(self.algorithm7tab, "")
        self.algorithm8tab = QtWidgets.QWidget()
        self.algorithm8tab.setObjectName("algorithm8tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.algorithm8tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.algorithm8 = QtWidgets.QComboBox(self.algorithm8tab)
        self.algorithm8.setObjectName("algorithm8")
        self.algorithm8.addItem("")
        self.algorithm8.addItem("")
        self.algorithm8.addItem("")
        self.algorithm8.addItem("")
        self.algorithm8.addItem("")
        self.algorithm8.addItem("")
        self.verticalLayout.addWidget(self.algorithm8)
        self.RRTimeQ8 = QtWidgets.QSpinBox(self.algorithm8tab)
        self.RRTimeQ8.setMinimum(1)
        self.RRTimeQ8.setObjectName("RRTimeQ8")
        self.verticalLayout.addWidget(self.RRTimeQ8)
        self.tabWidget.addTab(self.algorithm8tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 2)
        self.output1 = QtWidgets.QTextBrowser(self.widgetOutput)
        self.output1.setMinimumSize(QtCore.QSize(111, 131))
        self.output1.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.output1.setObjectName("output1")
        self.gridLayout_2.addWidget(self.output1, 0, 3, 6, 1)
        self.gridLayout.addWidget(self.widgetOutput, 0, 0, 1, 1)

        self.retranslateUi(CPU_Scheduler)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CPU_Scheduler)

    def retranslateUi(self, CPU_Scheduler):
        _translate = QtCore.QCoreApplication.translate
        CPU_Scheduler.setWindowTitle(_translate("CPU_Scheduler", "Form"))
        self.processInput.setHtml(_translate("CPU_Scheduler", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.processInput.setPlaceholderText(_translate("CPU_Scheduler", "process input .csv"))
        self.run_btn.setText(_translate("CPU_Scheduler", "Run"))
        self.writeData_btn.setText(_translate("CPU_Scheduler", "Write Data"))
        self.coreCount.setWhatsThis(_translate("CPU_Scheduler", "<html><head/><body><p>coreCount</p></body></html>"))
        self.coreCount_lbl.setText(_translate("CPU_Scheduler", "Core Count"))
        self.algorithm1.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm1.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm1.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm1.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm1.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm1.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm1tab), _translate("CPU_Scheduler", "Algorithm 1"))
        self.algorithm2.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm2.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm2.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm2.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm2.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm2.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm2tab), _translate("CPU_Scheduler", "Algorithm 2"))
        self.algorithm3.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm3.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm3.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm3.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm3.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm3.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm3tab), _translate("CPU_Scheduler", "Algorithm 3"))
        self.algorithm4.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm4.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm4.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm4.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm4.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm4.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm4tab), _translate("CPU_Scheduler", "Algorithm 4"))
        self.algorithm5.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm5.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm5.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm5.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm5.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm5.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm5tab), _translate("CPU_Scheduler", "Algorithm 5"))
        self.algorithm6.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm6.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm6.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm6.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm6.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm6.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm6tab), _translate("CPU_Scheduler", "Algorithm 6"))
        self.algorithm7.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm7.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm7.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm7.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm7.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm7.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm7tab), _translate("CPU_Scheduler", "Algorithm 7"))
        self.algorithm8.setItemText(0, _translate("CPU_Scheduler", "None"))
        self.algorithm8.setItemText(1, _translate("CPU_Scheduler", "FCFS"))
        self.algorithm8.setItemText(2, _translate("CPU_Scheduler", "RR"))
        self.algorithm8.setItemText(3, _translate("CPU_Scheduler", "SPN"))
        self.algorithm8.setItemText(4, _translate("CPU_Scheduler", "SRT"))
        self.algorithm8.setItemText(5, _translate("CPU_Scheduler", "HRRN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.algorithm8tab), _translate("CPU_Scheduler", "Algorithm 8"))
        self.output1.setHtml(_translate("CPU_Scheduler", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.output1.setPlaceholderText(_translate("CPU_Scheduler", "Output Box 1"))


        self.run_btn.clicked.connect(self.run_btn_clicked)
        self.writeData_btn.clicked.connect(self.writeData_btn_clicked)

    def run_btn_clicked(self):
        processInputLocation = self.processInput.toPlainText()
        processInputLocation = processInputLocation.replace('file:///', '')
        with open(processInputLocation) as f:
             reader = csv.reader(f)
        if not reader in self.files:
            self.files.append(processInputLocation)
            self.getflag()
            self.mastercontrol()
            """thread1 = myThread(1, "Thread-1", 1)
            thread1.start()
            thread1.join()"""
        #output42 = test.passedVariables(self, reader, coreCount, queueCount, algorithm1, algorithm2, algorithm3, algorithm4, algorithm5, algorithm6, algorithm7, algorithm8, RRTimeQ1, RRTimeQ2, RRTimeQ3, RRTimeQ4, RRTimeQ5, RRTimeQ6, RRTimeQ7, RRTimeQ8)
    def writeData_btn_clicked(self):
        self.writedata()

    def getflag(self):
        TQ = []
        TQ.append(str(self.RRTimeQ1.value()))
        TQ.append(str(self.RRTimeQ2.value()))
        TQ.append(str(self.RRTimeQ3.value()))
        TQ.append(str(self.RRTimeQ4.value()))
        TQ.append(str(self.RRTimeQ5.value()))
        TQ.append(str(self.RRTimeQ6.value()))
        TQ.append(str(self.RRTimeQ7.value()))
        TQ.append(str(self.RRTimeQ8.value()))
    
        algorithms = []
        algorithms.append(str(self.algorithm1.currentText()))
        algorithms.append(str(self.algorithm2.currentText()))
        algorithms.append(str(self.algorithm3.currentText()))
        algorithms.append(str(self.algorithm4.currentText()))
        algorithms.append(str(self.algorithm5.currentText()))
        algorithms.append(str(self.algorithm6.currentText()))
        algorithms.append(str(self.algorithm7.currentText()))
        algorithms.append(str(self.algorithm8.currentText()))

        queueslength = 8
        for a in algorithms:
            if a == "None":
                queueslength -= 1
        stringthing = ""
        i = 0
        for a in algorithms:
            if a == "None":
                continue
            stringthing += a
            if a == "RR":
                stringthing += " "+TQ[i]
            stringthing += ","
            if i >= queueslength-1:
                break
            i += 1
        stringthing += "Cores:"+str(self.coreCount.value())
        self.usedflag = stringthing
                

    def mastercontrol(self):
        flag = self.usedflag
        processInputLocation = self.files[len(self.files)-1]
        #for processInputLocation in self.files:
        with open(processInputLocation) as f:
                datafilereader = csv.reader(f)
                pnum = self.coreCount.value()
                results = Overlord.Overlord(datafilereader,flag,pnum)
                print(results)
                if not flag in self.turnaroundresults:
                    self.turnaroundresults[flag] = []
                    self.waitresults[flag] = []
                    self.responseresults[flag] = []
                    self.throughputresults[flag] = []
                self.turnaroundresults[flag].append(results[0])
                self.waitresults[flag].append(results[1])
                self.responseresults[flag].append(results[2])
                self.throughputresults[flag].append(results[3].copy())
                print(self.throughputresults)
                self.output()
                
                #print("Simulation Complete. Results:",results)


    def writedata(self):
        try:
            with open('turnaroundresults.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for element in self.turnaroundresults:
                    writer.writerow([element,sum(self.turnaroundresults[element])/len(self.turnaroundresults[element])])
            with open('waitresults.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for element in self.waitresults:
                    writer.writerow([element,sum(self.waitresults[element])/len(self.waitresults[element])])
            with open('responseresults.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for element in self.responseresults:
                    writer.writerow([element,sum(self.responseresults[element])/len(self.responseresults[element])])
            with open('throughputresults.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for element in self.throughputresults:
                    writer.writerow([element,self.throughputresults[element]])
        except:
            print("Error writing to files.")

    def output(self):
        print("a")
        tnum = []
        wnum = []
        rnum = []
        thnum = []
        tnames = []
        wnames = []
        rnames = []
        thnames = []
        for element in self.turnaroundresults:
            tnames.append(element)
            tnum.append(sum(self.turnaroundresults[element])/len(self.turnaroundresults[element]))
        for element in self.waitresults:
            wnames.append(element)
            wnum.append(sum(self.waitresults[element])/len(self.waitresults[element]))
        for element in self.responseresults:
            rnames.append(element)
            rnum.append(sum(self.responseresults[element])/len(self.responseresults[element]))
        for element in self.throughputresults:
            print (element)
            thnames.append(element)
            thnum.append(self.throughputresults[element])

        print(thnum)
        output1This = "Turnaround Time\n"
        output2This = "\nWait Time\n"
        output3This = "\nResponse Time\n"
        output4This = "\nThroughput\n"
        i = 0
        for element in tnames:
            output1This += element + " "
            output2This += element + " "
            output3This += element + " "
            output4This += element + " "
            output1This += str(tnum[i]) + " "
            output2This += str(wnum[i]) + " "
            output3This += str(rnum[i]) + " "
            output4This += str(thnum[i]) + " "
            output1This += "\n"
            output2This += "\n"
            output3This += "\n"
            output4This += "\n"
            i += 1

        self.output1.setText(str(output1This)+str(output2This)+str(output3This)+str(output4This))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_CPU_Scheduler()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

