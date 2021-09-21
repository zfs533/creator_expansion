#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    生成垃圾函数代码
    原理：向ts源文件中插入垃圾代码，不影响原代码功能
    使用方法：在script同级目录打开终端执行 python createGarbage.py 
        第一步：备份原文件
        第二部：植入垃圾代码
"""
import random
import string
import os
import sys
import shutil


def createGarbage(order):
    """
        生成垃圾代码
        参数：
            order:生成垃圾函数方式命令，0含function声明，1不含function声明
        返回值：
            垃圾代码字符串
    """
    rd = random.randint(1, 9)
    varName = ''.join(random.sample(string.ascii_letters, rd))
    rdm = random.randint(5, 20)
    funcName = ''.join(random.sample(string.ascii_letters, rdm))
    rds = random.randint(1, 60)
    codeStr = ''.join(random.sample(string.ascii_letters + string.digits, rds))
    mm = ""
    if order == 0:
        mm = "function " + funcName + \
            "()"+"{\n\t"+"let "+varName+" = " + \
            "\"" + codeStr+"\"" + "\n}"+"\n"
    elif order == 1:
        mm = "" + funcName + \
            "()"+"{\n\t"+"let "+varName+" = " + \
            "\"" + codeStr+"\"" + "\n}"+"\n"
    return mm


def dealFile(ffile):
    """ 
        读写文件操作，写入垃圾代码
        参数：
            ffile:文件路径string
    """
    contentList = []
    for line in open(ffile):
        index1 = line.find("}")
        index2 = line.find("{")
        index3 = line.find("{}")
        contentList.append(line)
        if index1 > -1 and index2 > -1 and index3 < 0:
            contentList.append(createGarbage(0))
    rds = random.randint(20, 60)
    for i in range(rds):
        contentList.append(createGarbage(0))

    """ 先清空再写入 """
    fil = open(ffile, "r+")
    fil.truncate()
    fil = open(ffile, "a")
    for content in contentList:
        fil.write(content)
    fil.close()


def batchCopy():
    """
        备份script原始文件
    """
    scripts = ("%s/%s") % (os.getcwd(), "script")
    destination = ("%s/%s") % (os.getcwd(), "originScript")
    isExists = os.path.exists(destination)
    """ 只有第一次的时候备份，无需重复备份 """
    if not isExists:
        shutil.copytree(scripts, destination)


if __name__ == '__main__':
    """
        遍历script目录下的所有ts文件
    """
    batchCopy()
    paths = ("%s/%s") % (os.getcwd(), "script")
    for root, dirs, files in os.walk(paths):
        for k in files:
            length = len(k)
            extents = k[length-3:length]
            if(extents == ".ts"):
                dealFile(root+"/"+k)
