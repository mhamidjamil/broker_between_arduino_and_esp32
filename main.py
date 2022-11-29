import serial
import time
import re

# Setting serial port to COM4 at bard rate of 9600
port = serial.Serial('COM15', 115200)
port_out = serial.Serial('COM3', 115200)

# function that capture value  between < and > and print:

# def get_value(testStr):
#     print("data to fetch : ")
#     print(testStr)
#
#     fetched_data = re.findall("\d+\.\d+", testStr)
#     print(fetched_data)

# loop that call get_value(testString) every 1 second


while (1):
    # read data from port and print:
    # print(port.readline())
    # wait 1 second
    while (1):
        testString = port.readline()
        # print(testString)
        # printing type of input:
        # print(type(testString.decode()))
        # get_value(testString)
        # finalData {}

        # for temperature sensor :
        temperature_data = re.findall("<1_(.*)_1>", testString.decode())
        finalData = temperature_data[0].encode()
        port_out.write(temperature_data[0].encode())
        finalData += "!".encode()



        # for position sensor :
        position_data = re.findall("<2_(.*)_2>", testString.decode())
        finalData += position_data[0].encode()
        finalData += "!".encode()

        # for GSR sensor :
        GSR_data = re.findall("<3_(.*)_3>", testString.decode())

        finalData += GSR_data[0].encode()
        finalData += "!".encode()


        # for Snore sensor :
        Snore_data = re.findall("<4_(.*)_4>", testString.decode())
        finalData += Snore_data[0].encode()
        finalData += "!".encode()


        print(finalData)
        # print(type(finalData))

        # print(type(fetched_data))
        # port_out.write(fetched_data[0].encode())
        # print(fetched_data)
        time.sleep(1)
