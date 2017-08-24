#/usr/bin/python
#encoding:utf-8
import os
import time
import csv


class Controller(object):
    def __init__(self,count):
        self.counter = count
        self.alldata = [("timeatamp","cpustatus")]


    def testprocess(self):
        result = os.popen("adb shell dumpsys cpuinfo | grep com.weima.run.dev")
        for line in result.readlines():
            cpuvalue = line.split("%")[0]

        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime,cpuvalue))


    def run(self):
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1
            time.sleep(3)


    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime

    def SaveDataToCSV(self):
        csvfile = open('cpustatus.csv',"w",encoding="utf-8")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(5)
    controller.run()
    controller.SaveDataToCSV()