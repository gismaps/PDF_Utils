"""
Welcome to pdf_utils. The purpose of this package is to fix problems
with scanned PDF documents. 

**Note** - pdf_utils contains a module 'PDF' which contains a class also 
named 'PDF'. Since pdf_utils.PDF.PDF seemed redundant, this package 
imports the PDF class. The documentation still shows the extra PDF
module in the middle, but just import the class like this: 

```
from pdf_utils import PDF
``` 
"""

from .PDF import PDF

name = "pdf_utils"
__version__ = '0.0.1'    
__author__ = 'David Askov <https://www.linkedin.com/in/davidaskov/>'

