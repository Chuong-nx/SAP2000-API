"""Attach to a running instance of SAP2000"""

import sys
import comtypes.client
from tkinter import messagebox
import constants

def connect_to_sap_v19():
    try:
        # get the active SapObject
        mySapObject = comtypes.client.GetActiveObject("CSI.SAP2000.API.SapObject")
        # create sap_model object
        sap_model = mySapObject.SapModel
        return sap_model
    except (OSError, comtypes.COMError):
        messagebox.showerror(constants.TITLE, "Open the SAP model before starting the tool.")
        sys.exit(-1)

def connect_to_sap_v24():
    try:
        # create API helper object
        helper = comtypes.client.CreateObject('SAP2000v1.Helper')
        helper = helper.QueryInterface(comtypes.gen.SAP2000v1.cHelper)
        # get the active SapObject
        mySapObject = helper.GetObject("CSI.SAP2000.API.SapObject") 
        # create sap_model object
        sap_model = mySapObject.SapModel
        return sap_model
    except (OSError, comtypes.COMError):
        messagebox.showerror(constants.TITLE, "Open the SAP model before starting the tool.")
        sys.exit(-1)

sap_model = connect_to_sap_v19()
