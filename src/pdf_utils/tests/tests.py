'''
Unit tests for the package
'''

from pdf_utils.tests import test_config
from pdf_utils.PDF import PDF

from pathlib import Path

import inspect
import shutil
import unittest


class TestPDF(unittest.TestCase):
    """
    Unit tests for the pdf_utils.PDF.   
    
    Usage:
        I usually run unit tests in my Python IDE (PyDev). You can also
        run them from the command line in a variety of ways:  
        
        ```
        >cd /src/pdf_utils/tests
        >python tests.py  # invoke __main__ method via file name
        >python -m unittest tests.py # invoke as unittest via file name
        >python -m unittest -v pdf_utils.tests.tests.TestPDF # invoke via class
        ```
        
    Notes: 
        Most of these operations modify a PDF file. Validating that was
        done correctly might be possible to code, but is getting outside
        the scope of this little project. For that reason, tests may end
        with a hard-wired assert that will always succeed, but we're 
        really just testing that code hasn't raised any exceptions. It
        is recommended to manually verify your PDF results.  
    """

    def setUp(self):
        '''
        Read test config settings. 
        '''
        
        # First, we need to find the location of our sample PDFs for
        # testing. I don't want to use absolute paths, since everyone
        # can check out the repo to a different location. Tests can be
        # run from any package level, so we cannot use the current 
        # working directory from Python to make a relative path. We use 
        # the location of this file and navigate up to the project root.
        test_path = Path(__file__).resolve() # This test file
        levels_to_root = test_config['inputs']['levels_to_root']
        self.root_path = test_path.parents[levels_to_root-1]
        self.test_data_path = self.root_path / test_config[
                'inputs']['test_data_path']
        
        # Inputs
        self.pdf1 = self.test_data_path / test_config['inputs']['pdf1']
        self.pdf1_len = int(test_config['inputs']['pdf1_len'])
        self.pdf2 = self.test_data_path / test_config['inputs']['pdf2']
        
        # Outputs
        self.output_path = Path(test_config['outputs']['path'])

        
    def test_PDF_length(self):
        '''
        Test that a PDF is the correct length (number of pages). 
        '''
        pdf = PDF(str(self.pdf1))
        pdf_len = pdf.page_count
        msg = 'PDF page count {} is not the expected {}'.format(
                pdf_len, self.pdf1_len)
        self.assertTrue(pdf_len == self.pdf1_len, msg)


    def test_reverse_defaults(self):
        '''
        Test reversing with no inputs.
        '''
        def_name = inspect.currentframe().f_code.co_name
        out_file = self.output_path / (def_name + '.pdf')
        shutil.copy(self.pdf1, str(out_file))
        pdf = PDF(str(out_file))
        pdf.reverse(out_path=out_file)
        self.assertTrue(True, 'Unable to reverse the PDF document')


    def test_reverse_outpath(self):
        '''
        Test reversing while saving to a new file.
        '''
        pdf = PDF(str(self.pdf1))
        def_name = inspect.currentframe().f_code.co_name
        out_file = self.output_path / (def_name + '.pdf')
        pdf.reverse(out_path=out_file)
        self.assertTrue(True, 'Unable to reverse the PDF document')


    def test_interleave_defaults(self):
        '''
        Test the interleave() function with default parameters.
        
        Since this overwrites the input file, the first step is to make
        a copy of it. 
        '''
        def_name = inspect.currentframe().f_code.co_name
        out_file = self.output_path / (def_name + '.pdf')
        shutil.copy(self.pdf1, str(out_file))
        
        pdf1 = PDF(str(out_file))
        pdf2 = PDF(str(self.pdf2))
        pdf1.interleave(pdf2)


    def test_interleave_outpath(self):
        '''
        Test the interleave() function with an output path.
        '''
        def_name = inspect.currentframe().f_code.co_name
        out_file = self.output_path / (def_name + '.pdf')
        pdf1 = PDF(str(self.pdf1))
        pdf2 = PDF(str(self.pdf2))
        pdf1.interleave(pdf2, out_path=str(out_file))


    def test_interleave_first(self):
        '''
        Test the interleave() function with first=False parameter.
        '''
        def_name = inspect.currentframe().f_code.co_name
        out_file = self.output_path / (def_name + '.pdf')
        shutil.copy(self.pdf1, str(out_file))
        pdf1 = PDF(str(out_file))
        pdf2 = PDF(str(self.pdf2))
        pdf1.interleave(pdf2, first=False)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPDF']
    unittest.main()

