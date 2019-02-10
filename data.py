import random

def data_pull():
        hr = random.randint(48, 122)
        bp1 = random.randint(118, 142)
        bp2 = random.randint(78, 92)
        bo = random.randint(68, 112)

        pdata = {
                "heart_rate": hr,
                "blood_pressure1": bp1,
                "blood_pressure2": bp2,
                "blood_oxygen": bo,
        }
        return pdata
