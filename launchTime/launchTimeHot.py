#/user/bin/python
#encoding:utf-8
import csv
#执行命令的方法在os中
import os
import time


class App(object):
    def __init__(self):
        self.content = ""
        self.startTime = 0

    def launchApp(self):
        cmd = 'adb shell am start -W -n com.weima.run.dev/com.weima.run.SplashScreenActivity'
        self.content = os.popen(cmd)

    def stopApp(self):
        cmd = "adb shell input keyevent 3"
        #cmd = 'adb shell am force-stop com.weima.run.dev'
        os.popen(cmd)

    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime"in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime


class Controller(object):
    def __init__(self,count):
        self.app = App()
        self.counter = count
        self.allData = [("TimeStamp","ElapsedTime")]

    def testprocess(self):
        self.app.launchApp()
        time.sleep(5)
        elapsedTime = self.app.GetLaunchedTime()
        self.app.stopApp()
        time.sleep(3)
        currentTime = self.getCurrentTime()
        self.allData.append((currentTime,elapsedTime))

    def run(self):
        while self.counter>0:
            self.testprocess()
            self.counter = self.counter - 1

    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime


    def SaveDataToCSV(self):
        csvfile = open('startTimeHot.csv', "w", encoding="utf8")
        #csvfile = open('startTime.csv','wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.allData)
        csvfile.close()

if __name__ == "__main__":
    controller = Controller(10)
    controller.run()
    controller.SaveDataToCSV()


#热启动启动时间性能（与冷启动相比，改关闭命令和文件名）