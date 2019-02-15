def get_intervals():
    print("Enter time in seconds")
    hr = int(input("Enter the interval for heart rate: "))
    bp = int(input("Enter the interval for systolic blood pressure: "))
    bp2 = int(input("Enter the interval for diastolic blood pressure: "))
    bo = int(input("Enter the interval for blood oxygen: "))
    return hr, bp, bp2, bo
