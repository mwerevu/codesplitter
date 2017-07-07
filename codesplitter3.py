import re
import pprint

class Chunk:
    'Chunk class is a generic bit of a program.'

    def __init__(self):
        self.parentprogname=""
        self.chunkcontents=""
        self.chunktype=""
        
    def getChunk():
        return self.chunkcontents

    def getType():
        return self.chunktype

class CodeChunk(Chunk):
    'Specific chunk class to hold code.'

    def __init__(self):
        self.chunktype="code"
        
class CommentChunk(Chunk):
    'Specific chunk class to hold comment.'

    def __init__(self):
        self.chunktype="comment"
        
class DataChunk(Chunk):
    'Specific chunk class to hold a SAS data block.'

    def __init__(self,inputcode):
        self.chunktype="data"
        
        # Search for an input dataset.
        # The model is:    (?P<ds>\(\.*\))
        #testset=re.findall(r'\w*(\(\.*\))*',inputcode,flags=re.MULTILINE)
        test1=re.search(r'(?:set )(?P<dataline>\s*.*?)(?:;)',inputcode,flags=re.M|re.S)
        if test1:
            print test1.group('dataline')
            test2=re.findall(r'(\w|\.)+?',test1.group('dataline'),flags=re.M|re.S)
            test2=re.split(r'(\(.*?\)|\s+)',test1.group('dataline'),flags=re.M|re.S)
            if test2:
                print test2
                
        inset=re.search(r'(?<=set )\s*(?P<ds>(\w|\.)+)',inputcode,flags=re.MULTILINE)
        if inset:
            self.indatasets=inset.group('ds')
        else:
            inds="(FAIL)"
            
        # Search for an output dataset.
        outset = re.search(r'\s*(?P<ds>(\w|\.)+)',inputcode,flags=re.MULTILINE)
        if outset:
            self.outdatasets=outset.group('ds')
            self.creatortype="set"
        else:
            self.outdatasets="(NONE)"
            self.creatortype="(NONE)"

            
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

    def __init__(self,thisChunk):
        self.chunktype="proc"
        proctype = re.match(r'^(\w|\.)+',thisChunk)
        if proctype:
            self.proctype=proctype.group(0)
        else:
            self.proctype="(NONE)"
        self.indatasets=None
        self.outdatasets=None

        

    



class CodeSplit:
    'CodeSplit class for chunked program. Contains a list of chunks.'
    
    def __init__(self,origname,origcode):
        self.name = origname
        self.chunks=[]
        chunks = re.split(r'(data |proc )',origcode)

        prev = ""
        for chunk in chunks:
            if prev == "DATA":
                self.chunks.append(DataChunk(chunk))
                #print "%s --DATA(SET)--> %s" % (dataflow[0],dataflow[1])
            elif prev == "PROC":
                self.chunks.append(ProcChunk(chunk))
                #print "PROC Block: Type = %s" % proctype.group(0)
            # Prep for next chunk.
            if chunk == "data ":
                prev="DATA"
            elif chunk == "proc ":
                prev="PROC"
            else:
                prev=""
        
    def getChunks(self):
        for chunk in self.chunks:
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(chunk.__dict__)
            #print chunk.__dict__
    
    
### Main Section of Code
# Open program.
orig = open("./dataflowcases.sas","r")
prog = orig.read()

# Create a new program object.
p1=CodeSplit("Test1",prog)
p1.getChunks()


        
