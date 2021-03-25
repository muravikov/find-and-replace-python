#!/usr/bin/python
# coding: utf8

import sys,os, fnmatch, codecs

def log_err(message):
    with open('1.log','a') as f:
        f.write(message+'\n')

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath,'r') as f:
                s = f.read()
            try:
                s = s.decode('utf8')
            except:
                print()
                error_msg = '!error utf8 decode:'+filepath
                print(error_msg)
                log_err(error_msg)
                print()
                pass
                continue
            s = s.replace(find, replace)
            with open(filepath, 'w') as f:
                f.write(s.encode('utf8'))
                print(filepath),
                print('                                                                                         \r'),

# read from file pattern replace
file_pattern = open('!patterntext.txt','r')
replce_pattern = file_pattern.read().decode('utf8')
file_pattern.close()

# read from file text for replace
file_find_pattern = open('!findtext.txt','r')
find_pattern = file_find_pattern.read().decode('utf8')
file_find_pattern.close()

findReplace('.',find_pattern,replce_pattern,'*.html')
print()