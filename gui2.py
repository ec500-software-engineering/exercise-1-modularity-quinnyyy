from tkinter import *
from data import pdata
from error_handler import Error_Handler
from alert_system import page_doctor
from datastore import insertData
import time
import random
import asyncio

data = pdata()
loop = asyncio.get_event_loop()

def runUI2(hr_interval,bp_interval,bp2_interval,bo_interval):
    window = Tk()
    hr = IntVar()
    bp = IntVar()
    bp2 = IntVar()
    bo = IntVar()

    trueVals = [0,0,0,0]

    window.title("EC500 Health Montior System")

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

    async def get_new_data():
        #print("getting new data")
        data.generate()
        await asyncio.sleep(random.randint(1,5)/10)

    async def after_gen():
        while True:
            await get_new_data()
            mydata = data.get()
            update_data(mydata)
            errors(mydata)
            insertData(10,mydata)

    def update_data(mydata):
        #print("updating data")
        trueVals[0] = mydata["heart_rate"]
        trueVals[1] = mydata["blood_pressure1"]
        trueVals[2] = mydata["blood_pressure2"]
        trueVals[3] = mydata["blood_oxygen"]

    def errors(mydata):
        #print("errors")
        warning, identifier = Error_Handler(mydata)
        page_doctor(mydata,identifier,warning)

    def update_hr():
        hr.set(trueVals[0])
        window.after(1000*hr_interval,update_hr)

    def update_bp():
        bp.set(trueVals[1])
        window.after(1000*bp_interval,update_bp)

    def update_bp2():
        bp2.set(trueVals[2])
        window.after(1000*bp2_interval,update_bp2)

    def update_bo():
        bo.set(trueVals[3])
        window.after(1000*bo_interval,update_bo)

    async def tk_update():
        while True:
            window.update()
            await asyncio.sleep(.1)

    update_hr()
    update_bp()
    update_bp2()
    update_bo()
    loop.create_task(tk_update())
    loop.create_task(after_gen())
    #loop.create_task(update_hr())
    #loop.create_task(update_bp())
    #loop.create_task(update_bp2())
    #loop.create_task(update_bo())
    loop.run_forever()
