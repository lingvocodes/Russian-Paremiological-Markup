#!/usr/bin/python
# -*- coding:  utf-8' -*-
#Filename: paremio_markup.py


import codecs
import re


def Fopen(fileName):
    try:
        file = codecs.open(fileName, 'r', 'utf-8-sig') 
        return file
    except IOError: 
        print "error %s opening %s" % (IOError, fileName) 
#стандартный метод на открытие файлов
def Fwrite(fileName):
    try:
        rffd = codecs.open(fileName, 'w', 'utf-8-sig') 
        return rffd
    except IOError:
        print "error %s opening %s" % (IOError, fileName)
# открываем или создаем новый файл в случае отсутствия

def Poslov(file):     # вводный аргумент - файл с пословицами
    slvr=[]
    i=0
    f=Fopen(file)
    for line in f:
        line=line.strip()
        slvr.append(line)
    f.close()
    print "Словарь пословиц загружен! "
    return slvr
# метод, создающий из файла словарь пословиц, загружается в буффер   

def Prover(fileName, slvr):  
    f=Fopen(fileName)
    ff=f.read()
    newName=u"New_"+fileName
    for i in slvr:
        posl=ur""
        line=i.split(u" ")
        for l in line: 
            posl +=ur""+l+u"? ?\\W? ?" 
        inew = u" <parem>"+i+u"</parem> "
        regx = re.compile(posl,re.I |re.U)
        m = regx.findall(ff)
        if m!= None: 
            slvr=m
            for ux in slvr:
                print "Найдена пословица:"
                print ux
        ff=regx.sub(inew,ff)
    m=Fwrite(newName)
    m.write(ff)
    f.close()
    m.close()
    return
Prover(u'Пример.txt',Poslov(u'пословицы.txt'))


