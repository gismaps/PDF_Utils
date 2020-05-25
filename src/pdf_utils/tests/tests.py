'''
Created on May 9, 2020

@author: david
'''


from pdf_utils import PDF

from pathlib import Path

import configparser
import shutil
import unittest


class TestPDF(unittest.TestCase):

    def setUp(self):
        config = configparser.ConfigParser()
        config.read('../../data/tests/test_config.ini')
        self.test_file_path = Path(config['PATHS']['test_file_path'])
        self.pdf1 = self.test_file_path / config['PATHS']['pdf1']
        self.pdf1_len = int(config['PATHS']['pdf1_len'])
        self.pdf2 = self.test_file_path / config['PATHS']['pdf2']
        self.output_path = Path(config['PATHS']['output_path'])
        self.interleave_file1 = self.output_path / config['PATHS'][
            'interleave_file1'] 
        self.interleave_file2 = self.output_path / config['PATHS'][
            'interleave_file2'] 
        self.reverse_file = self.output_path / config['PATHS']['reverse_file'] 
        
    def testPDF(self):
        pdf = PDF(str(self.pdf1))
        pdf_len = pdf.page_count
        msg = 'PDF page count {} is not the expected {}'.format(
                pdf_len, self.pdf1_len)
        self.assertTrue(pdf.page_count == self.pdf1_len, msg)

    def testReverse(self):
        pdf = PDF(str(self.pdf1))
        pdf.reverse(self.reverse_file)

    def testInterleave(self):
        shutil.copy(self.pdf1, self.interleave_file1)
        
        pdf1 = PDF(str(self.interleave_file1))
        pdf2 = PDF(str(self.pdf2))
        pdf1.interleave(pdf2)

    def testInterleave2(self):
        pdf1 = PDF(str(self.pdf1))
        pdf2 = PDF(str(self.pdf2))
        pdf1.interleave(pdf2, out_path=self.interleave_file2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPDF']
    unittest.main()

