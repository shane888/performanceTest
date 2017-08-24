#/usr/bin/python
#encoding:utf-8

import os
import time
import  csv


class Controller(object):
    def __init__(self,count):
        self.counter = count
        self.alldata = [("timestamp","power")]

    def testprocess(self):
        result = os.popen("adb shell dumpsys battary")
        for line in result:
            if "level" in line:
                power =line.split(":")[1]

        currrenttime = self.getCurrentTime
        self.alldata.append(("currenttime","power"))

    def run(self):
        if self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

        time.sleep(5)

    def getCurrentTime(self):
        currenttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currenttime

    def saveDataToCSV(self):
        csvfile = open('power.csv',"wb",ecoding="utf-8")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__" :
    controller = Controller(10)
    controller.run()
    controller.saveDataToCSV()