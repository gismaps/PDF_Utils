---
description: |
    API documentation for modules: pdf_utils, pdf_utils.PDF, pdf_utils.tests, pdf_utils.tests.test_config, pdf_utils.tests.tests.

lang: en

classoption: oneside
geometry: margin=1in
papersize: a4

linkcolor: blue
links-as-notes: true
...


    
# Module `pdf_utils` {#pdf_utils}

Welcome to pdf_utils. The purpose of this package is to fix problems
with scanned PDF documents. 

**Note** - pdf_utils contains a module <code>[pdf\_utils.PDF](#pdf\_utils.PDF "pdf\_utils.PDF")</code> which contains a class of
the same name. In order to remove the extra '.PDF' from the module
structure, this package imports the PDF class, so you can import the
PDF class as <code>[pdf\_utils.PDF](#pdf\_utils.PDF "pdf\_utils.PDF")</code>.


    
## Sub-modules

* [pdf_utils.PDF](#pdf_utils.PDF)
* [pdf_utils.tests](#pdf_utils.tests)






    
# Module `pdf_utils.PDF` {#pdf_utils.PDF}

Module for PDF utilities.





    
## Classes


    
### Class `PDF` {#pdf_utils.PDF.PDF}



> `class PDF(file_path: str)`


An object that represents a single PDF file. 

Contains utilities to solve basic problems, like reversing the 
order of the pages in a scan.  


#### Args

**```file_path```** :&ensp;<code>str</code>
:   The path to the PDF file.



#### Returns

<code>A [PDF](#pdf\_utils.PDF.PDF "pdf\_utils.PDF.PDF") object. </code>
:   &nbsp;

#### Raises

<code>OSError</code>
:   If the file_path parameter does not exist 


**```Note```**
:   The pdf_utils module imports this class directly,
    so don't add the extra '.PDF' for the module it's in.


**```Example```**
:   How to import and instantiate:
    
        from pdf_util import PDF
        my_pdf = PDF('/path/to/file.pdf')







    
#### Instance variables


    
##### Variable `page_count` {#pdf_utils.PDF.PDF.page_count}

Page count for the PDF document

    
##### Variable `path` {#pdf_utils.PDF.PDF.path}

The path to the PDF file.

###### Raises 

OSError: When setting this property, OSError is raised if
    the file is not found at the specified path.



    
#### Methods


    
##### Method `interleave` {#pdf_utils.PDF.PDF.interleave}



    
> `def interleave(self, pdf: <module 'pdf_utils.PDF' from 'C:\\git\\PDF_Utils\\src\\pdf_utils\\PDF.py'>, first: bool = True, out_path: str = None) -> NoneType`


Interleave the pages from another PDF with this one. 

Use case is a two-sided paper doc scanned to separate PDFs for
the front and back. Notes: 

- If one PDF is longer than the other, additional of the pages 
  from the longer document will be consecutively added at the
  end. 
- The output will overwrite this PDF object's file. 


###### Args

**```pdf```**
:   Another PDF object with pages to interleave with
    this object. Must be of type <code>[pdf\_utils.PDF](#pdf\_utils.PDF "pdf\_utils.PDF")</code>.


**```first```**
:   Optional bool, default=True. In the interleave
    ordering, should this object's pages come first (True, 
    i.e.: pages 1, 3, 5...) or second (False, i.e.: pages 
    2, 4, 6...)?


**```out_path```**
:   Optional string, default=None. If supplied,
    the output will be saved to this path, instead of
    overwriting this PDF object's path.



###### Returns

<code>None</code>
:   &nbsp;

###### Raises

<code>No exceptions raised </code>
:   &nbsp;

###### Examples

Invoke like this to overwrite this PDF's file:

```>>> my_pdf.interleave('/files/even_pages.pdf')```

Save the output to a new file:

```>>> my_pdf.interleave('./even_pages.pdf', 
out_path='./combo.pdf')```

Normally, this PDF object's pages come first, but you can
also make the incoming PDF's pages come first, instead:

```>>> my_pdf.interleave('/files/odd_pages.pdf', 
first=False)```

    
##### Method `reverse` {#pdf_utils.PDF.PDF.reverse}



    
> `def reverse(self, out_path: str = None) -> NoneType`


Reverse the page order (from last to first) of the PDF. 


###### Note

The default settings this will overwrite this object's PDF
file.


###### Args

**```out_path```**
:   Optional string, default=None. If supplied,
    the output will be saved to this path, instead of
    overwriting this PDF object's path.



###### Returns

<code>None</code>
:   &nbsp;

###### Raises

<code>No exceptions raised </code>
:   &nbsp;

###### Examples

Invoke like this to overwrite this PDF's file:

```>>> my_pdf.reverse()```

Pass in a path to save as a new file. 

```>>> my_pdf.reverse('/path/to/new/file.pdf')```



    
# Module `pdf_utils.tests` {#pdf_utils.tests}

This module contains unit tests for the pdf_utils module. You only need
this if you are contributing to this module's code, but it might be
useful as example code.


    
## Sub-modules

* [pdf_utils.tests.test_config](#pdf_utils.tests.test_config)
* [pdf_utils.tests.tests](#pdf_utils.tests.tests)






    
# Module `pdf_utils.tests.test_config` {#pdf_utils.tests.test_config}

This file is configuration for the unit tests. It contains one item,
a dict named <code>test\_config</code>. Import it like this: 

```from pdf_utils.tests import test_config```







    
# Module `pdf_utils.tests.tests` {#pdf_utils.tests.tests}

Unit tests for the package





    
## Classes


    
### Class `TestPDF` {#pdf_utils.tests.tests.TestPDF}



> `class TestPDF(methodName='runTest')`


Unit tests for the pdf_utils.PDF.   


#### Usage

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

Create an instance of the class that will use the named test
method when executed. Raises a ValueError if the instance does
not have a method with the specified name.


    
#### Ancestors (in MRO)

* [unittest.case.TestCase](#unittest.case.TestCase)






    
#### Methods


    
##### Method `setUp` {#pdf_utils.tests.tests.TestPDF.setUp}



    
> `def setUp(self)`


Read test config settings.

    
##### Method `test_PDF_length` {#pdf_utils.tests.tests.TestPDF.test_PDF_length}



    
> `def test_PDF_length(self)`


Test that a PDF is the correct length (number of pages).

    
##### Method `test_interleave_defaults` {#pdf_utils.tests.tests.TestPDF.test_interleave_defaults}



    
> `def test_interleave_defaults(self)`


Test the interleave() function with default parameters.

Since this overwrites the input file, the first step is to make
a copy of it.

    
##### Method `test_interleave_first` {#pdf_utils.tests.tests.TestPDF.test_interleave_first}



    
> `def test_interleave_first(self)`


Test the interleave() function with first=False parameter.

    
##### Method `test_interleave_outpath` {#pdf_utils.tests.tests.TestPDF.test_interleave_outpath}



    
> `def test_interleave_outpath(self)`


Test the interleave() function with an output path.

    
##### Method `test_reverse_defaults` {#pdf_utils.tests.tests.TestPDF.test_reverse_defaults}



    
> `def test_reverse_defaults(self)`


Test reversing with no inputs.

    
##### Method `test_reverse_outpath` {#pdf_utils.tests.tests.TestPDF.test_reverse_outpath}



    
> `def test_reverse_outpath(self)`


Test reversing while saving to a new file.


-----
Generated by *pdoc* 0.8.1 (<https://pdoc3.github.io>).
