import openpyxl
import os
from configparser import ConfigParser
import re
from datetime import datetime


class brake_the_code(Exception): pass


config = ConfigParser()
config.read("setting.ini")


ip = config.get("configuration", "target_ip")
Excel_file = config.get("configuration","Excel_file")
sheet_name = config.get("configuration","Sheet_Name")

def file_writer(data):
    file = open("report.txt", 'w')
    file.write(data)
    file.close()

os.system("echo" + " the given target ip address is {0}".format(ip))
os.system(" cd reports")

try:
    book = openpyxl.load_workbook(Excel_file)
    #file = open("report.txt", 'w')

    sheet = book.active
    sheet2 = book[sheet_name]

    for row in sheet2.values:
        for value in row[:3]:

            if value is None:
                file_writer(" no command is found : please input the test command in the XL in required format ")
                raise brake_the_code

            if value == 'Action' or value == "TC description" or value == "Command":
                pass

            else:
                if row.index(value) == 0:
                    file_writer(value + "\n")

                if row.index(value) == 1:
                    test_name = value
                    os.system("echo " + " ---------- " + str(value) + " -------------- ")
                    file_writer(test_name + "\n")

                if row.index(value) == 2:
                    value = re.sub("<IP>", ip, value)
                    file_writer("command --> " + value + "\n")
                    dateTimeObj = datetime.now()
                    timestampStr = dateTimeObj.strftime("%d-%b-%Y")
                    os.system("echo" + " command_is -------------- " + str(value) + " -------------- ")
                    os.system(value + " -oX " + test_name + ".xml | tee -a report.txt && xsltproc " + test_name + \
                              ".xml  -o " + test_name +"-"+timestampStr+ ".html")

        file_writer(80 * "-")
        file_writer("\n")

except brake_the_code:
    os.system("echo " + "exiting the code because of Null value")
    file_writer("exiting the code because of Null value" + "\n")

except Exception:
    file_writer(str(Exception) + "\n")
    os.system("echo" + str(Exception))

print("************* the test is completed against the host {0}*****************".format(ip))
