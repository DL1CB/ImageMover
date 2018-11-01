# Image Mover

A Python script to move images into date folders
This is specifically desigend for SD cards
used by digital camera's

The script will walk down the directory tree
of the source, looking for and *.jpg files.

if needed it will then create a date directory in the
destination and move the image file accross

e.g xyz.jpg ->  /2018-10-27/xyz.jpg

Usage

python main.py source dest

e.g. pyhon main.py F: D:\MyImageFolder
