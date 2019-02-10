import random

def data_pull():
        hr = random.randint(55, 125)
        bp1 = random.randint(115, 145)
        bp2 = random.randint(78, 92)
        bo = random.randint(65, 115)

        pdata = {
                "heart_rate": hr,
                "blood_pressure1": bp1,
                "blood_pressure2": bp2,
                "blood_oxygen": bo,
        }
        return pdata
