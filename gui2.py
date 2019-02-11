from tkinter import *
from data import data_pull
from error_handler import Error_Handler
from alert_system import page_doctor
from datastore import insertData
import time
import random


def runUI(hr_interval,bp_interval,bp2_interval,bo_interval):
    window = Tk()

    hr = IntVar()
    bp = IntVar()
    bp2 = IntVar()
    bo = IntVar()

    test = [0,0,0,0] #hr, bp, bp2, bo

    window.title("EC500 Health Monitor System")

    label1 = Label(window, text='Heart Rate')
    label1.grid(row=0, column=0)
    textBox1 = Label(window, height=2, width=10, textvariable = hr)
    textBox1.grid(row=1, column=0)

    label2 = Label(window, text='Systolic Blood Pressure')
    label2.grid(row=0, column=1)
    textBox2 = Label(window, height=2, width=10, textvariable = bp)
    textBox2.grid(row=1, column=1)

    label2 = Label(window, text='Diastolic Blood Pressure')
    label2.grid(row=0, column=2)
    textBox2 = Label(window, height=2, width=10, textvariable = bp2)
    textBox2.grid(row=1, column=2)

    label3 = Label(window, text='Blood Oxygen')
    label3.grid(row=0, column=3)
    textBox3 = Label(window, height=2, width=10, textvariable = bo)
    textBox3.grid(row=1, column=3)

    def update_pdata():
        pdata = data_pull()
        warning, identifier = Error_Handler(pdata)
        page_doctor(pdata,identifier,warning)
        #I wasn't really sure how the encryption works so I didn't include it but it would go here
        insertData(10,pdata) #arbitrary patient_id of 10
        test[0] = pdata["heart_rate"]
        test[1] = pdata["blood_pressure1"]
        test[2] = pdata["blood_pressure2"]
        test[3] = pdata["blood_oxygen"]
        window.after(1000, update_pdata)

    def update_hr():
        hr.set(test[0])
        window.after(1000, update_hr)

    def update_bp():
        bp.set(test[1])
        window.after(2000, update_bp)

    def update_bp2():
        bp2.set(test[2])
        window.after(5000, update_bp2)

    def update_bo():
        bo.set(test[3])
        window.after(10000, update_bo)

    update_pdata()
    update_hr()
    update_bp()
    update_bp2()
    update_bo()

    window.mainloop()
