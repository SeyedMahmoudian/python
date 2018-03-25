"""
File Name: MyTest.py
Author: Seyedamin Seyedmahmoudian
ID: 040813340
Course: CST8333 - Programming Language Research Project
Version : 4
Assignment:Final
Professor: Stanley Pieda
Since: 3.6
Date : 2017-12-17
"""
"""
This class is only made to demonstrate how unit testing works in python
It will check if file name has been send to processor correctly or not

"""
import unittest

try:
    import processor as processor  # object of processor
except ImportError:
    import processor as processor


class MyTest(unittest.TestCase):
    table = ""
    filename = ""

    def testFileName(self):
        self.filename = "./dataset.csv"
        self.assertEqual(processor.returnFile(self.filename), self.filename)
