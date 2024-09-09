'''
Created on Jan 19, 2023

@author: MaramJehad
'''
import unittest
import app

class SbomTest(unittest.TestCase):


    def testSbom_shouldReturnAuthorID(self):
        myName = "mza0200"
        result = app._getAuthor("../../")
        ResultAuthorName = result['author']
        self.assertEqual(ResultAuthorName, myName)


