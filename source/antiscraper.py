#!/usr/bin/env python3

# -*- coding: UTF-8 -*-


import cgi
import cgitb; cgitb.enable()
import os, re


def main(): # NEW except for the call to processInput
    form = cgi.FieldStorage()      # standard cgi script lines to here!

    '''
    # use format of next two lines with YOUR names and default data
    numStr1 = form.getfirst("x", "0") # get the form value associated with form
                                   # name 'x'.  Use default "0" if there is none.
    numStr2 = form.getfirst("y", "0") # similarly for name 'y'
    contents = processInput(numStr1, numStr2)   # process input into a page
    print(contents)
    '''


    arguments = cgi.FieldStorage()
    print('arg:',arguments)
    #for i in arguments.keys():
    #    print('<br>',arguments[i],arguments[i].value)


    testdir = '2'
    indexfile = 'index.html'
    content = fileToStr(os.path.join(testdir, indexfile))

    ## change all links to python script arguments
    content = changeLinks(content)

    print(content.encode("utf-8"))


# standard code for future cgi scripts from here on
def fileToStr(fileName):
    """Return a string containing the contents of the named file."""

    fin = open(fileName, encoding="utf-8")
    contents = fin.read()
    fin.close()
    return contents


def changeLinks(content):
    content = re.sub('href=\"', 'href=\"?url=', content)
    return content



try:   # NEW
    print("Content-type: text/html\n\n")   # say generating html
    main()
except:
    cgi.print_exception()                 # catch and print errors