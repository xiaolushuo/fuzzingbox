#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import subprocess
import sys
from time import sleep

def runWebTest():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("fuzzing - 无前提下直接进行黑盒,选择你的目标:  \n 1: 谷歌 \n 2: 火狐 \n 3: 洋葱")
    browserType = input('>>')
    timeout = input(
        "设置响应时间，建议区间30以上::")
    checkValidBrowserType(browserType)
    for root, folders, fileNames in os.walk("recurve"):
        for fileName in fileNames:
            if not fileName.endswith('.html'):
                continue
            processCommand = getBrowserApplication(browserType)
            if processCommand is not None:
                setupExploit(dir_path, fileName, processCommand, root)
                runExploit(processCommand, timeout)
            else:
                print "无法对这类浏览器进行fuzzing!"

def runExploit(processCommand, timeout):
    print "执行命令: " + " ".join(processCommand)
    process = subprocess.Popen(processCommand)
    sleep(timeout)
    print "关闭黑盒中的浏览器进程"
    process.kill()
    sleep(3)


def setupExploit(dir_path, fileName, processCommand, root):
    filePath = os.path.join(dir_path, root, fileName)
    filePath = "file://" + filePath
    print "Testing with exploit:" + filePath
    processCommand.append(filePath)


def getBrowserApplication(browserType):
    if browserType == 1:
        processCommand = ['google-chrome']
    elif browserType == 2:
        processCommand = ['firefox', '--new-instance']
    elif browserType == 3:
        processCommand = ['start-tor-browser']
    else:
        processCommand = None
    return processCommand


def checkValidBrowserType(browserType):
    if browserType not in [1, 2, 3]:
        print("你的本机没有安装这款浏览器，我真的搞不定啊!")
        sys.exit(0)


if __name__ == '__main__':
    runWebTest()
