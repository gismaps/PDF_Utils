'''
Module for PDF utilities. 
'''

from pdf_utils import PDF 

from pathlib import Path
from pdfrw import PdfReader, PdfWriter
#from pdfrw import  IndirectPdfDict # for file metadata


class PDF(object):
    '''
    An object that represents a single PDF file. 
    
    Contains utilities to solve basic problems, like reversing the 
    order of the pages in a scan.  
    
    **Note** - This 'PDF' class technically resides in a module of the
    same name. Since the pdf_utils package imports this class, you
    should skip the extra 'PDF' in the import, like this: 

    ```
    from pdf_utils import PDF
    ``` 
    
    '''

    # TODO: Subset pages
    
    # TODO: Rotate pages
    
    # TODO: Catch PermissionError exception for locked files? 
    
    # TODO: Get/set metadata
    #    in_pdf.keys()
    #    in_pdf.Info
    #    type(in_pdf.Info) <class 'pdfrw.objects.pdfdict.PdfDict'>
    #
    #    This copied the metadata, but was breaking everything else 
    #    trailer = pdf1_reader
    #    if not first: trailer = pdf2_reader
    #    outdata.write(trailer=trailer)  

    def __init__(self, file_path:str):
        '''
        Args:
            file_path (str): The path to the PDF file.

        Returns:
            A PDF object. 
    
        Raises:
            OSError: If the file_path parameter does not exist 

        Example: 
            How to import and instantiate:
            
                from pdf_util import PDF
                my_pdf = PDF('/path/to/file.pdf')
        '''
        self.__path = None
        self.path = file_path
        
        #TODO: Add pages property & save method?  
        # By design, these methods are very simple and self-contained. When they
        # run, output is saved immediately. For scaling up, it could be more 
        # efficient to chain several operations together (saving the latest
        # collection of pages to a property), and then save when ready.  
        
    @property
    def path(self) -> str:
        '''
        The path to the PDF file.
        
        ## Raises 
        
        OSError: When setting this property, OSError is raised if
            the file is not found at the specified path.
        '''
        
        return self.__path
    
    @path.setter
    def path(self, file_path:str):
        '''
        Path setter 
        
        Args:
            file_path (str): File path
            
        Raises:
            OSError: If the path set does not exist. 
        '''
        p = Path(file_path)
        if not p.exists():
            raise(OSError("Input path does not exist: {}".format(file_path)))
        self.__path = file_path
    
    @property
    def page_count(self) -> int:
        '''
        Page count for the PDF document
        '''
        pages = PdfReader(self.path).pages
        return len(pages)

    def reverse(self, out_path:str = None) -> None:
        '''
        Reverse the page order (from last to first) of the PDF. 
        
        Note:
            The default settings this will overwrite this object's PDF
            file.

        Args:
            out_path: Optional string, default=None. If supplied,
                the output will be saved to this path, instead of
                overwriting this PDF object's path.

        Returns:
            None
    
        Raises:
            No exceptions raised 
        
        Examples:
            Invoke like this to overwrite this PDF's file:
            
            ```>>> my_pdf.reverse()```

            Pass in a path to save as a new file. 
             
            ```>>> my_pdf.reverse('/path/to/new/file.pdf')```
        '''

        if not out_path: out_path = self.path
        outdata = PdfWriter(out_path)
        in_pdf = PdfReader(self.path)
        pages = in_pdf.pages
        for i in range((len(pages)-1), -1, -1):
            outdata.addpage(pages[i])
        
        outdata.write()
        
        

    def interleave(self, pdf:PDF, first:bool = True, 
                   out_path:str = None) -> None:
        '''
        Interleave the pages from another PDF with this one. 
        
        Use case is a two-sided paper doc scanned to separate PDFs for
        the front and back. Notes: 
        
        - If one PDF is longer than the other, additional of the pages 
          from the longer document will be consecutively added at the
          end. 
        - The output will overwrite this PDF object's file. 

        Args:
            pdf: Another PDF object with pages to interleave with
                this object. Must be of type `pdf_utils.PDF`.
            first: Optional bool, default=True. In the interleave
                ordering, should this object's pages come first (True, 
                i.e.: pages 1, 3, 5...) or second (False, i.e.: pages 
                2, 4, 6...)?
            out_path: Optional string, default=None. If supplied,
                the output will be saved to this path, instead of
                overwriting this PDF object's path.

        Returns:
            None
    
        Raises:
            No exceptions raised 
        
        Examples:
            Invoke like this to overwrite this PDF's file:
             
            ```>>> my_pdf.interleave('/files/even_pages.pdf')```

            Save the output to a new file:
             
            ```>>> my_pdf.interleave('./even_pages.pdf', 
            out_path='./combo.pdf')```

            Normally, this PDF object's pages come first, but you can
            also make the incoming PDF's pages come first, instead:
             
            ```>>> my_pdf.interleave('/files/odd_pages.pdf', 
            first=False)```
        '''
        pdf1_path = self.path  # this object's path
        pdf2_path = pdf.path   # incoming object's path
        if not first: # incoming file comes first, reverse the order
            pdf1_path = pdf.path
            pdf2_path = self.path
        pdf1_reader = PdfReader(pdf1_path)
        pdf1_pages = pdf1_reader.pages
        pdf1_len = len(pdf1_pages)
        pdf2_reader = PdfReader(pdf2_path)
        pdf2_pages = pdf2_reader.pages
        pdf2_len = len(pdf2_pages)
        
        if not out_path: out_path = self.path
        outdata = PdfWriter(out_path)

        for i in range(0, pdf1_len):
            outdata.addPage(pdf1_pages[i])
            if (i+1) > pdf2_len: continue # no more pages in pdf2
            outdata.addPage(pdf2_pages[i])
        
        if pdf2_len > pdf1_len: # out of pages in pdf1, but more in pdf2
            for i in range(pdf1_len, pdf2_len):
                outdata.addPage(pdf2_pages[i])
        
        outdata.write()
