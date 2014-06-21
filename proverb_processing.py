#!/usr/bin/python
# -*- coding:  utf-8' -*-
#Filename: proverb_processing.py

# данный модуль предназначен для предварительной работы 
# со списком пословиц и преведения его в надлежащий, готовый
# для использования вид

import codecs

def Fopen(fileName):
    try:
        rffd = codecs.open(fileName, 'r', 'utf-8-sig') 
        return rffd
    except IOError: 
        print "error %s opening %s" % (IOError, fileName) 
# стандартный метод, открывающий файл, используя модуль codecs

def Fwrite(fileName):
    try:
        rffd = codecs.open(fileName, 'w','utf-8-sig') 
        return rffd
    except IOError: 
        print "error %s opening %s" % (IOError, fileName) 
# метод, открывающий файл или создающий новый

def Povtor(fileName, fileNew):
    list=[]
    s=0
    f = Fopen(fileName)
    for line in f:
        s+=1
        line=line.lower().strip()
        if line not in list:list.append(line)
    print s
    print len(list)
    m=Fwrite(fileNew)  
    for e in list:
        m.write(e+'\n') 
    f.close() 
    m.close()     
    return
#Povtor(u'adam.txt',u'Пословицы.txt')
# метод, с помощью которого избавляемся от повторов в списке пословиц

def Chistka(fileName,fileNew):
    list=[]
    nline = " "
    s=0
    f=Fopen(fileName)
    for line in f:
        s+=1
        line=line.strip()
        if line[-1] == u"." and nline == " ":
            list.append(line)
        elif line[-1] == u"." and nline != "":
            line = nline+u" "+line
            nline =" "
            list.append(line)
        else:nline=line
    print s,len(list)
    f.close()
    m=Fwrite(fileNew)
    for e in list: m.write(e+"\n") 
    m.close()     
    return
#Chistka(u'Пословицы.txt',u'new.txt')
# метод соединяет "оторванные" куски пословиц с идущими перед ними в списке

def Skobki(fileName,fileNew):
    list=[]
    s=0
    f=Fopen(fileName)
    for line in f:
        line=line.strip()
        if u"(" in line and u")" in line and s==0:
            sx=line.index(u'(')
            sy=line.index(u')')
            nline=line[:sx-1]+line[sy+1:] 
            list.append(nline)
        if u"(" in line and u")" not in line and s==0:
            s=1
            nline=line
        if u")" in line and s==1:
            s=0
            line=nline+" "+line
            list.append(line)
        if u"(" not in line and u")" not in line and s==0:
            list.append(line) 
    m=Fwrite(fileNew)
    print len(list)
    for e in list: m.write(e+"\n") 
    m.close()     
    return
#Skobki(u"skobki.txt",u"nskobki.txt")
# метод, удаляющий скобки
# после работы данного метода, для точности была проделана проверка по файлу вручную
# чтобы убедиться, что все пословицы написаны без скобок
 
def Dlina(fileName,fileNew):
    list=[]
    s=0
    f=Fopen(fileName)
    for line in f:
        line=line.strip()
        if line[-1]!= u".": print line   #проверяем, все ли строки заканчиваются на точку 
        line=line[:-1]   #убираем точки в конце всех строк
        if u"." in line:
            s+=1
            nline=line.split()   #разбиваем строки на слова
            for i in nline:   
                if i[0]==u".": #если точка перед словом-просто лишняя
                    tt=line.index(u".")
                    tline=line[:tt]+line[tt+1:]
                    list.append(tline)
            else:    #если нет, то разбиваем строки по точке
                line=line.split(u".")
                for i in line: 
                    i=i.strip()
                    print i
                    list.append(i)
        else: list.append(line)
    print len(list)
    m=Fwrite(fileNew)
    for e in list: m.write(e+"\n") 
    f.close()
    m.close()     
    return
#Dlina(u"nskobki.txt",u"nposlovs.txt")
# этот метод позволил разбить строки с несколькими пословицами 
# а также удалить лишние точки
# тут снова вручную отредактировали строки, которые не оканчиваются точкой
# (предварительно выведя их на экран)


def Skley(fileName,fileNew):
    list=[]
    f=Fopen(fileName)
    ss=0
    for line in f:
        ss+=1
        line=line.strip()
        list.append(line)
        if len(line)<=10:
            print ss, line
    nlist=list.sort(key=len) 
    f.close()
    m=Fwrite(fileNew) 
    for e in list: m.write(e+"\n") 
    m.close()
    return
    
#Skley(u"nposlovs.txt",u"slovar.txt")
# этим методом создаем служебный файл для проверки строк    
# на наличие обрывков или пустых строк
# самые короткие строки и пустые выводятся на экран
       
        