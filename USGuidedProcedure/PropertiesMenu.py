'''
Created on 29/03/2013

@author: Usuario
'''
import os

from __main__ import vtk, qt, ctk, slicer


class PropertiesMenu(qt.QWidget):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        qt.QWidget.__init__(self)
        self.propertiesMenuWidget=qt.QTableWidget(3,2)
        #self.checkBoxVisible2D = qt.QCheckBox()
        #self.checkBoxVisible2D.setTristate(False)
        self.checkBoxVisible3D = qt.QCheckBox()
        self.checkBoxVisible3D.setTristate(False)
        self.colourButton=qt.QPushButton("...")
        self.meshOpacitySlider = qt.QSlider()
        self.meshOpacitySlider.setObjectName("meshOpacityScrollBar")
        self.meshOpacitySlider.setMaximum(100)
        self.meshOpacitySlider.setMinimum(1)
        self.meshOpacitySlider.setValue(100)
        self.meshOpacitySlider.setOrientation(1) #horizontal
        #self.propertiesMenuWidget.setCellWidget(0,0,qt.QLabel("Visible2D"))
        #self.propertiesMenuWidget.setCellWidget(0,1,self.checkBoxVisible2D)
        self.propertiesMenuWidget.setCellWidget(0,0,qt.QLabel("Visible3D"))
        self.propertiesMenuWidget.setCellWidget(0,1,self.checkBoxVisible3D)
        self.propertiesMenuWidget.setCellWidget(1,0,qt.QLabel("Color"))
        self.propertiesMenuWidget.setCellWidget(1,1,self.colourButton)
        self.propertiesMenuWidget.setCellWidget(2,0,qt.QLabel("Opacity"))
        self.propertiesMenuWidget.setCellWidget(2,1,self.meshOpacitySlider)
        
        
    def show(self):
        self.propertiesMenuWidget.show()    