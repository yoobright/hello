# -*- coding: utf-8 -*-

def h():
    print 'Wen Chuan',
    m = yield 5 # Fighting!
    print m
    d = yield 12
    print 'We are together!'
c = h()
c1 = c.send(None) #相当于c.send(None)
print 'c1:' + str(c1)
c2 = c.send('Fighting!') #(yield 5)表达式被赋予了'Fighting!'输出的结果为：Wen Chuan Fighting!
print 'c2:' + str(c2)
c3 = c.send(None)
print 'c3:' + str(c3)