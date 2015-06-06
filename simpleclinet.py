# -*- coding: utf-8 -*-
# import  xmlrpclib
#
# if __name__ == '__main__':
#     # proxy = xmlrpclib.ServerProxy("http://localhost:7774/")
#     # proxy.hello()
#
#     proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
#     # print "3 is even: %s" % str(proxy.is_even(3))
#     # print "100 is even: %s" % str(proxy.is_even(100))
#     proxy.hello()

import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:7774', #verbose=True,
                              allow_none=True)
# print proxy.hello()
# print proxy.show()
# print proxy.add(3)
# print proxy.add(7)
# print proxy.show()
# print proxy.system.listMethods()
print proxy.system.methodHelp('show')
