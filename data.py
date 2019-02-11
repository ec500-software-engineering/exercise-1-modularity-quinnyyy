import random

def data_pull():
        hr = random.randint(49, 121)
        bp1 = random.randint(119, 141)
        bp2 = random.randint(79, 91)
        bo = random.randint(69, 111)

        pdata = {
                "heart_rate": hr,
                "blood_pressure1": bp1,
                "blood_pressure2": bp2,
                "blood_oxygen": bo,
        }
        return pdata
