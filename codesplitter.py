# Refs
# http://www.thegeekstuff.com/2014/07/python-regex-examples/
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# https://docs.python.org/2/library/re.html
# http://www.nltk.org/howto/chunk.html

import re
#import nltk
from pyparsing import Word, alphas

# Read in dummy program.
orig = open("./testcode01.sas","r")
prog = orig.read()


combined = re.split(r'(/\*BEGINCCC|CCCEND\*/\n)',prog,flags=re.DOTALL)
print "*** COMBINED ***"
#print combined
parseidx=0
parsedcode=[]
flag="CODE"
for idx,val in enumerate(combined):
#    parsedcode
    if val == "/*BEGINCCC":
        flag="COMMENT"
    elif val == "CCCEND*/\n":
        flag="CODE"
    else:
        commlines = len(re.findall(r'\n',val))
        parsedcode.append([parseidx,flag,idx,commlines,val])
        parseidx+=1
        
        

        
for chunk in parsedcode:
    print chunk


    
quit()


# Used standard regex parsing.
#matches = re.split(r'\/\*BEGINCCC',orig.read())
#print matches

opening = re.findall(r'^.*?(?=/\*BEGINCCC)',prog,flags=re.DOTALL)
comments = re.findall(r'(?<=/\*BEGINCCC).*?(?=CCCEND\*/)',prog,flags=re.DOTALL)
code = re.findall(r'(?<=CCCEND\*/).*?(?=/\*BEGINCCC)',prog,flags=re.DOTALL)

# This one doesn't work yet.
closing = re.findall(r'(?<=CCCEND\*/).*(?<!/\*BEGINCCC)\Z',prog,flags=re.DOTALL)

print "*** OPENING ***"
for idx,val in enumerate(opening):
    print idx,val
print "*** COMMENTS ***"
for idx,val in enumerate(comments):
    print idx,val
print "*** CODE ***"
for idx,val in enumerate(code):
    print idx,val
print "*** CLOSING ***"
for idx,val in enumerate(closing):
    print idx,val



# pyparsing
# define grammar
greet = Word( alphas ) + "," + Word( alphas ) + "!"

# input string
hello = "Hello, World!"

# parse input string
print hello, "->", greet.parseString( hello )
