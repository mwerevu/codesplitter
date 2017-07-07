# codesplitter2
#
# This program is meant to parse de-macroized SAS code into network data about the datasets.
# Nodes will be datasets and edges will be generalized descriptions of how one gets from one dataset to another. (Initial idea, merges and splits may be problematic.)
#
# Classes:
# - DATA block with single SET. - 80%
# - DATA block with multiple SETs. - 50%
# - DATA block with MERGE - 0%
# - DATA block with INFILE - 0%
# - DATA block with DATALINES - 0%
# - PROC SUMMARY/MEANS - 0%
# - PROC FREQ - 0%
# - PROC IMPORT - 0%
# - PROC EXPORT - 0%
# - Others?


import re

#orig = open("./debug.sas","r")
orig = open("./dataflowcases.sas","r")
prog = orig.read()



def parseDataChunk(thisChunk):
    outset = re.search(r'(?<=set )\s*(?P<ds>(\w|\.)+)',thisChunk,flags=re.MULTILINE)
    if outset:
        outds=outset.group('ds')
    else:
        outds="(FAIL)"
    inset = re.search(r'\s*(?P<ds>(\w|\.)+)',thisChunk,flags=re.MULTILINE)
    if inset:
        inds=inset.group('ds')
    else:
        inds="(NONE)"
    return [inds,outds]




mixed = re.split(r'(data |proc )',prog)
#print mixed
prev = ""
for idx,chunk in enumerate(mixed):
    print chunk
    if prev == "DATA":
        dataflow = parseDataChunk(chunk)
        print "%s --DATA(SET)--> %s" % (dataflow[0],dataflow[1])

#        outset = re.match(r'^(\w|\.)+',chunk)
#        print "DATA Block: Output = %s" % outset.group(0)
#        inset = re.search(r'(?<=set )(\w|\.)+',chunk)
#        if inset:
#            print "Input = %s" % inset.group(0)
    elif prev == "PROC":
        proctype = re.match(r'^(\w|\.)+',chunk)
        print "PROC Block: Type = %s" % proctype.group(0)

    # Prep for next chunk.
    if chunk == "data ":
        prev="DATA"
    elif chunk == "proc ":
        prev="PROC"
    else:
        prev=""
