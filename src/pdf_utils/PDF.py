'''
Created on May 9, 2020

@author: david
'''

from pathlib import Path
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict
from pdf_utils import PDF

class PDF(object):
    '''
    PDF utilities to solve basic problems. These are mostly meant to
    solve scanning problems, but could evolve from there.  
    '''


    def __init__(self, file_path:str):
        '''
        Constructor
        '''
        self.__path = None
        self.path = file_path
        
        #TODO: Consider saving intermediate results before saving. 
        # The approach was to create simple, self-contained methods, saving the
        # PDF after each call. For high-volume operations, it would be more
        # efficient to enable the consumer to perform several operations and
        # then save only when ready.  Add a property for pages here?
        
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, file_path:str):
        p = Path(file_path)
        if not p.exists():
            raise(OSError("Input path does not exist: {}".format(file_path)))
        self.__path = file_path
    
    @property
    def page_count(self):
        '''
        Page count for the PDF document
        '''
        pages = PdfReader(self.path).pages
        return len(pages)

    def reverse(self, out_path:str = None) -> None:
        '''
        Reverse the page order (from last to first) of the PDF. The
        output metadata will be copied from this PDF object.
        There is no return value from this function.  
        :param out_path: Optional string, default=None. If supplied,
            the output will be saved to this path. The default is to
            over-write this PDF object's path. 
        '''
        if not out_path: out_path = self.path
        outdata = PdfWriter(out_path)
        in_pdf = PdfReader(self.path)
        pages = in_pdf.pages
        for i in range((len(pages)-1), -1, -1):
            outdata.addpage(pages[i])
        outdata.write(trailer=in_pdf)
        
        

    def interleave(self, pdf:PDF, second:bool = True, 
                   out_path:str = None) -> None:
        '''
        Interleave the pages from another PDF with this one. Use case
        is a two-sided paper doc scanned to two PDFs for front and
        back. Note that if one PDF is longer than the other, the rest of
        the pages from the longer document will be consecutively added
        at the end. The output metadata will be copied from this PDF
        object.
        There is no return value from this function.  
        :param pdf: Another PDF object with pages to interleave with
            this object. 
        :param second: Optional bool, default=True. If True, the input
            PDF will have its pages come second, i.e.: pages 2,4,6... If
            False, they will come first, i.e.: pages 1,3,5...
        :param out-path: Optional string, default=None. If this 
            parameter is supplied, the output will be saved to this
            path. Otherwise, this object's path will be over-written.
        '''
        pdf1_path = self.path  # this object's path
        pdf2_path = pdf.path   # incoming object's path
        if not second: # incoming file comes first, reverse the order
            pdf1_path = pdf.path
            pdf2_path = self.path
        pdf1_reader = PdfReader(pdf1_path)
        pdf2_reader = PdfReader(pdf2_path)
        pdf1_pages = pdf1_reader.pages
        pdf2_pages = pdf2_reader.pages
        pdf1_len = len(pdf1_pages)
        pdf2_len = len(pdf2_pages)
        trailer = pdf1_reader
        if not second: trailer = pdf2_reader
        
        if not out_path: out_path = self.path
        outdata = PdfWriter(out_path)

        for i in range(0, pdf1_len):
            outdata.addPage(pdf1_pages[i])
            if (i+1) > pdf2_len: continue # no more pages in pdf2
            outdata.addPage(pdf2_pages[i])
        
        if pdf2_len > pdf1_len: # out of pages in pdf1, but more in pdf2
            for i in range(pdf1_len, pdf2_len):
                outdata.addPage(pdf2_pages[i])
        
        # TODO: Preserve file metadata
        outdata.write(trailer=trailer)
            
    
    # TODO: Subset
    # TODO: Rotate
    # TODO: Catch PermissionError exception for locked files? 
    # TODO: Get/set metadata
    #    in_pdf.keys()
    #    in_pdf.Info
    #    type(in_pdf.Info) <class 'pdfrw.objects.pdfdict.PdfDict'>
