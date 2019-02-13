from data import pdata
import threading
import random

x = pdata()

def test(x):
    wait = random.randint(1,5)
    threading.Timer(wait, test, [x]).start()
    x.generate()
    print(x.pull())


test(x)
