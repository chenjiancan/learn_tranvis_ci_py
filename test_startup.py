# -*- coding: utf-8 -*-
__author__ = 'cjc'

import unittest
import startup

class MyTestCase(unittest.TestCase):
    def test_name(self):
        name = "myname"
        company = startup.Company(name)
        self.assertEqual(name, company.name())


if __name__ == '__main__':
    unittest.main()
