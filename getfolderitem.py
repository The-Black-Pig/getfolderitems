#!/usr/bin/env python3

from getpass import getuser
from tkinter import *
from tkinter import filedialog
from os import listdir


def folder():
    root = Tk()
    root.withdraw()  # get rid of annoying little window
    my_path = filedialog.askdirectory(initialdir="/Users/" + getuser(), title="Select Folder") + "/"
    return my_path


def pdffile():
    root = Tk()
    root.withdraw()  # get rid of annoying little window
    my_file = filedialog.askopenfilename(initialdir="/Users/" + getuser(), title="Select pdf file",
                                         filetypes=[("pdf file", "*.pdf")])
    return my_file


def jpgfile():
    root = Tk()
    root.withdraw()  # get rid of annoying little window
    my_file = filedialog.askopenfilename(initialdir="/Users/" + getuser(), title="Select jpg/jpeg file",
                                         filetypes=[("jpeg file", "*.jpg"), ("jpeg file", "*.jpeg")])
    return my_file

def tiffile():
    root = Tk()
    root.withdraw()  # get rid of annoying little window
    my_file = filedialog.askopenfilename(initialdir="/Users/" + getuser(), title="Select tif/tiff file",
                                         filetypes=[("tif file", "*.tif"), ("tiff file", "*.tiff")])
    return my_file

def pngfile():
    root = Tk()
    root.withdraw()  # get rid of annoying little window
    my_file = filedialog.askopenfilename(initialdir="/Users/" + getuser(), title="Select png file",
                                         filetypes=[("png file", "*.png")])
    return my_file


def txtfile():
    root = Tk()
    root.withdraw()  # get rid of annoying little window
    my_file = filedialog.askopenfilename(initialdir="/Users/" + getuser(), title="Select txt file",
                                         filetypes=[("text file", "*.txt")])
    return my_file

def anyfile():
    root = Tk()
    root.withdraw()  # get rid of annoying little window
    my_file = filedialog.askopenfilename(initialdir="/Users/" + getuser(), title="Select any file",
                                         filetypes=[])
    return my_file

def foldercontents(filetype):
    returnlist = []
    #  ending = "pdf"
    path_to_file = folder()
    if len(listdir(path_to_file)) != 0:
        file_list = listdir(path_to_file)  # fill list with file names

    for item in file_list:  # filter file names
        if item.endswith(filetype):
            returnlist.append(path_to_file + item)
        
    return returnlist