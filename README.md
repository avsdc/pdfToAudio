**Description:**


Import two libraries pyttsx3 and PyPDF2.

The pyttsx3.init() creates a speaker. speaker.setProperty sets the rate to 180.

In Part1, the page from the file "OliverTwist.pdf" is opened in the 'rb' mode. The PDFReader takes the book as argument 
to return a reader.
The reader.pages[0] returns the page to be read i.e. first and only page. Next, page.extract_text returns the text from
the page to be read. The speaker reads the text out.

In Part2, the page from the file "OliverTwist.pdf" is opened in the 'rb' mode, using the with open statement. The rest
of the code is similar to Part1.


In Part3, the page from the file "SOPHE_2023.pdf" is opened in the 'rb' mode. The PDFReader takes the book as argument 
to return a reader.
The reader.pages[0] returns the page to be read i.e. first and only page. Next, page.extract_text returns the text from
the page to be read. The speaker reads the text out. The speaker also saves the text to "myaudio.pdf" file.

In Part4, all the pages from the file "SOPHE_2023.pdf" are read into a string i.e. full_text. The statement len(reader.pages)
returns the number of pages in the file. In a for loop, each page's text is extracted and concatenated to the string "full_text".
The speaker reads it out.

In Part5, content from url(pdf file) is downloaded, read and math translated. The text is extracted. The result shows that the text
extraction is fine, but the math is not translated properly.


**Requirements:**

io
requests
pyttsx3
PyPDF2
PDFReader
 
