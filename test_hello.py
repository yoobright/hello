# -*- coding: utf-8 -*-
from oslotest import base
import hello


class Test(base.BaseTestCase):
    def setUp(self):
        super(Test, self).setUp()

    def test_hello(self):
        hello.hello_fun()

