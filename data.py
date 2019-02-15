import random
import time

class pdata:
    def __init__(self):
        self.hr = random.randint(49,121)
        self.bp1 = random.randint(119,141)
        self.bp2 = random.randint(79,91)
        self.bo = random.randint(69,111)

    def generate(self):
        time.sleep(random.randint(1,5))
        self.hr = random.randint(49,121)
        self.bp1 = random.randint(119,141)
        self.bp2 = random.randint(79,91)
        self.bo = random.randint(69,111)

    def get(self):
        data = {
                "heart_rate": self.hr,
                "blood_pressure1": self.bp1,
                "blood_pressure2": self.bp2,
                "blood_oxygen": self.bo,
        }
        return data
