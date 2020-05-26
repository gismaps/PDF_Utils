# PDF Utils
PDF Utilities to make common tasks a bit easier. Currently, it just contains
fixes I need for the documents produced by my one-sided scanner, but I may add
to it as time permits.  

There is only one class: `pdf_utils.PDF`. You can read all about it at the 
[GitHub Pages documentation](https://gismaps.github.io/PDF_Utils)
or by checking code out of GitHub and navigating to the `docs` folder. 

## Installation

Follow these steps to install pdf_utils into your Python environment: 
- Look in the `dist` folder for a .whl file. If there is more than one, locate
  the newest by version number. 
- Clone the Git repo or otherwise copy the .whl file to your hard drive. 
- At the command prompt, type the following command: 

  ```
  pip install /path/to/dist/pdf_utils-0.0.1-py3-none-any.whl
  ```
  
  Notes: 
  - If the pip command is not found, it is often located in the `Scripts` 
    folder under your Python install. 
  - The path is unnecessary if you run the `pip` command in the same directory
    as the .whl file. 
  - Update the file name in the command above with your .whl file name, 
    especially the version number. 
- Test your setup: 
	```
	>>> from pdf_utils import PDF
	>>> pdf = PDF('./pages.pdf')
	>>> pdf.reverse(out_path='./reversed.pdf')
	```  

## License
Distributed with the MIT license - see [LICENSE.txt](./LICENSE.txt). Note that 
this makes use of other packages with their own license agreements, most 
notably the [pdfrw package](https://pypi.org/project/pdfrw/). 
