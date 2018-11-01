#!/usr/bin/python3
import os, time, shutil, sys

try:
    sourcedir = sys.argv[1]
    destdir = sys.argv[2]
except:
    print('useage:')
    print('python main.py sourcedir destdir')
    print('python main.py F:\\ D:\\Sony')

def movefiles(sourcedir,destdir):
    for subdir, dirs, files in os.walk(sourcedir):
        for f in files: 
            if f.lower().endswith('.jpg'):
                fpath = '{}\{}'.format(subdir,f)
                ftime = time.gmtime(os.path.getmtime(fpath))
                
                ctime_dir = '{}\{}-{:02d}-{:02d}'.format(destdir, ftime.tm_year, ftime.tm_mon, ftime.tm_mday)
                if not os.path.isdir(ctime_dir):
                    print('create directory ',ctime_dir)
                    os.mkdir(ctime_dir)
                dest = '{}\{}'.format(ctime_dir,f)     
                shutil.move(fpath, dest);
                print('File {} has been moved to {}'.format(fpath,dest))
               
if __name__ == "__main__":
    movefiles(sourcedir,destdir)