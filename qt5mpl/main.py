from tesqt5designer import *
import sys 
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar ) 

import random
import numpy as np

class testqt5(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        #init
        self.update_graph()
        self.labels1.setText("Joint 1 Angle: "+str(self.hslider1.value())+u'\N{DEGREE SIGN}')
        self.labels2.setText("Joint 2 Angle: "+str(self.hslider2.value())+u'\N{DEGREE SIGN}')
        self.labels3.setText("Joint 3 Angle: "+str(self.hslider3.value())+u'\N{DEGREE SIGN}') 

        #process
        self.pushButton_graph.clicked.connect(self.update_graph)
        self.pushButton1.clicked.connect(self.showName1)
        self.pushButton2.clicked.connect(self.showName2)
        self.hslider1.valueChanged.connect(self.s1label)
        self.hslider2.valueChanged.connect(self.s2label)
        self.hslider3.valueChanged.connect(self.s3label)

    def clickMe(self):
        print("hellow dunia")
    def showName1(self):
        self.label1.setText("indra agustian")
    def showName2(self):
        self.label1.setText("apa kabar??")
    def s1label(self):
        self.labels1.setText("Joint 1 Angle: "+str(self.hslider1.value())+u'\N{DEGREE SIGN}')
    def s2label(self):
        self.labels2.setText("Joint 2 Angle: "+str(self.hslider2.value())+u'\N{DEGREE SIGN}')
    def s3label(self):
        self.labels3.setText("Joint 3 Angle: "+str(self.hslider3.value())+u'\N{DEGREE SIGN}')  

    def  update_graph(self): 
        fs  =  500 
        f  =  random.randint ( 1 ,  100 ) 
        ts  =  1 / fs 
        length_of_signal  =  100 
        t  =  np.linspace ( 0,1,length_of_signal ) 
        
        cosinus_signal  =  np.cos ( 2 * np.pi * f * t ) 
        sinus_signal  = np.sin ( 2 * np.pi * f * t ) 

        self.MplWidget.canvas.axes.clear () 
        self.MplWidget.canvas.axes.plot (t, cosinus_signal ) 
        self.MplWidget.canvas.axes.plot (t, sinus_signal ) 
        self.MplWidget.canvas.axes.legend (( 'cosinus', 'sinus' ), loc = 'upper right' ) 
        self.MplWidget.canvas.axes.set_title ( ' Cosinus - Sinus Signal' ) 
        self.MplWidget.canvas.draw()   


app = QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=testqt5(MainWindow)
MainWindow.show()
app.exec_()

