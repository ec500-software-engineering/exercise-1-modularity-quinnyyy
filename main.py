from gui import runUI
from error_handler import Error_Handler
from data import data_pull

pdata = data_pull()
print(pdata)
is_warning, identifier = Error_Handler(pdata)
print(is_warning)
print(identifier)
#runUI()
