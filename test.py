from data import pdata

test = pdata()
print(test.hr)

def change():
    test.generate()

change()
print(test.hr)
