In my job, I find myself constantly dealing with batches of pdf files, and sometimes
forced to write quick scripts on the fly to solve immediate problems.

I have also found that I constantly need the same routines again and again, so the best
idea was to pack them in a library available everwhere.

This sort of thing, is of course, well known to experienced programmers, and therefore
aimed primarily at newbies.

Getting started:

Find the folder/directory where Python holds all it's modules.

Start Python3 in terminal and type in the following:

	import sys

	print('\n'.join(sys.path))

This should return something like the following:

	/Library/Frameworks/Python.framework/Versions/3.5/lib/python35.zip
	/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5
	/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin
	/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload
	/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages

No matter which platform you are using, you will always get paths to common directories,
take a look at the contents of these directories and you will find some familiar file
names, these are the installed modules.

Now you can copy "getfolderitem.py" into one of these diectories, I personally like
/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5

Now run demo.py in Terminal, PyCharm, Eric or Idle (as you please)

The options in module "getfolderitem" are :-

.folder()	<b>path to folder</b><br>
.pdffile()	<b>path to pdf file</b><br>
.jpgfile()	<b>path to jpg/jpeg file</b><br>
.tiffile()	<b>path to tif/tiff file</b><br>
.pngfile()	<b>path to png file</b><br>
.txtfile()	<b>path to txt file</b><br>
.anyfile()	<b>path to any file</b><br>
.foldercontents("pdf") <b>returns a list of files in the selected folder, filters with file type e.g. "pdf"</b>

Author: Steve Clements
