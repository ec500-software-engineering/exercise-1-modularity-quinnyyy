# EC500 Health Monitor System
To run it: ```python3 main.py```

gui2 effectively acts as main.py so i just import it in main.py and call runUI with ask_intervals.
I wasn't sure how encryption/decryption modules worked so I just omitted those in my design.
I added ask_intervals module in my design.

User should input the intervals for each measurement to tell the GUI how often to update.
![intervals](/intervals.png?raw=true "intervals")

GUI displays heart rate, blood pressure, blood oxygen levels and updates at custom interval for each
![gui](/monitor.png?raw=true "gui")

If a data value is anomalous a message will be written to console (to simulate alerting doctor)
![alert](/alert.png?raw=true "alert")
