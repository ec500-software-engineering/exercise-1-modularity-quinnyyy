from gui import runUI
from error_handler import Error_Handler
from data import data_pull
from alert_system import page_doctor
import time

while True:
    time.sleep(2)
    pdata = data_pull()
    print(pdata)
    warning, identifier = Error_Handler(pdata)
    print(warning)
    print(identifier)
    page_doctor(pdata,identifier,warning)
#runUI()
