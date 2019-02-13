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

class pdata():

    hr = random.randint(49, 121)
    bp1 = random.randint(119, 141)
    bp2 = random.randint(79, 91)
    bo = random.randint(69, 111)

    def generate(self):
        self.hr = random.randint(49, 121)
        self.bp1 = random.randint(119, 141)
        self.bp2 = random.randint(79, 91)
        self.bo = random.randint(69, 111)

    def pull(self):
        return self.hr,self.bp1,self.bp2,self.bo
