# -*- coding: utf-8 -*-
# from SimpleXMLRPCServer import SimpleXMLRPCServer
# from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
#
# class RequestHandler(SimpleXMLRPCRequestHandler):
#     rpc_paths = ('/RPC2',)
#
# class DemoClass(object):
#     def __init__(self):
#         self.list = []
#
#     def add(self, a):
#         return self.list.append(a)
#
#     def show(self):
#         return self.list
#
# def hello():
#     print 'hello'
#
# if __name__ == '__main__':
#     server = SimpleXMLRPCServer(("localhost", 7774),
#                                 requestHandler=RequestHandler,
#                                 allow_none=True)
#     server.register_introspection_functions()
#     server.register_function(hello, "hello")
#     server.register_instance(DemoClass())
#     server.serve_forever()



