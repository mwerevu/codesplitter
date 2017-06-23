import re

class Chunk:
    'Chunk class is a generic bit of a program.'

    def __init__():
        self.parentprogname=""
        self.chunkcontents=""
        self.chunktype=""
        
    def getChunk(self):
        return self.chunkcontents

    def getType(self):
        return self.chunktype

class CodeChunk(Chunk):
    'Specific chunk class to hold code.'

    def __init__():
        self.chunktype="code"
        
class CommentChunk(Chunk):
    'Specific chunk class to hold comment.'

    def __init__():
        self.chunktype="comment"
        
class DataChunk(Chunk):
    'Specific chunk class to hold a SAS data block.'

    def __init__():
        self.chunktype="data"
        self.creatortype=None
        self.indatasets=None
        self.outdatasets=None


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

        
class ProcChunk(Chunk):
    'Specific chunk class to hold SAS proc block.'

    def __init__():
        self.chunktype="proc"
        self.proctype=None
        self.indatasets=None
        self.outdatasets=None

        

    



class CodeSplit:
    'CodeSplit class for chunked program. Contains a list of chunks.'
    
    def __init__():
        self.name=""
        self.chunks=[]

    def chunkProgram(self,origname,origcode):
        self.name = origname
        chunks = re.split(r'(data |proc )',origcode)

        prev = ""
        for idx,chunk in enumerate(chunks):
            if prev == "DATA":
                self.chunks.append(DataChunk())


                
                dataflow = parseDataChunk(chunk)
                print "%s --DATA(SET)--> %s" % (dataflow[0],dataflow[1])
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
prev = ""
for idx,chunk in enumerate(mixed):
    print chunk
    if prev == "DATA":
        dataflow = parseDataChunk(chunk)
        print "%s --DATA(SET)--> %s" % (dataflow[0],dataflow[1])
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
        
