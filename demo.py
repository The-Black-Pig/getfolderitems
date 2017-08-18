#!/usr/bin/env python3

import getfolderitem as fetch

# gets all files from selected folder that ends jpg
# and returns the paths in a list
my_list = fetch.foldercontents(".jpg")
# returns the path to selected pdf file
my_pdf = fetch.pdffile()

print(my_list)
print()
print(my_pdf)
