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

        ### FIRST, test for a "set" statement.
        test1=re.search(r"""(?:set\s+)           # Look for set statement + spaces and discard.
                            (?P<setline>.*?\s*)  # Look for whatever is in the middle.
                            (?=;)                # Look ahead for the ending semicolon.
                            """,inputcode,flags=re.M|re.S|re.X)
        if test1:
            test2=re.findall(r"""(?:\s*)     # Find a discard any leading spaces
                                 ([\.\w]*)    # Find the dataset name, possibly with a period in it.
                                 (?:\(.*?\))* # Find an optional parenthetical and discard it.
                                 """,test1.group('setline'),flags=re.M|re.S|re.X)
            if test2:
                self.indatasets=[x for x in test2 if x != '']
                self.creatortype="set"
            else:
                self.indatasets=["(NONE)"]
                self.creatortype="(NONE)"
        else:
            ### IF NOT, test for a "merge" statement.
            test1=re.search(r"""(?:merge\s+)           # Look for set statement + spaces and discard.
                                (?P<setline>.*?\s*)  # Look for whatever is in the middle.
                                (?=;)                # Look ahead for the ending semicolon.
                                """,inputcode,flags=re.M|re.S|re.X)
            if test1:
                test2=re.findall(r"""(?:\s*)     # Find a discard any leading spaces
                                  ([\.\w]*)    # Find the dataset name, possibly with a period in it.
                                  (?:\(.*?\))* # Find an optional parenthetical and discard it.
                                  """,test1.group('setline'),flags=re.M|re.S|re.X)
                if test2:
                    self.indatasets=[x for x in test2 if x != '']
                    self.creatortype="merge"
                else:
                    self.indatasets=["(NONE)"]
                    self.creatortype="(NONE)"
                
            
        ### NOW, get output datasets.
        outset = re.search(r'\s*(?P<ds>[\w\.]+)',inputcode,flags=re.MULTILINE)

        test1=re.search(r"^.*?;",inputcode,flags=re.M|re.S)
        if test1:
            test2=re.findall(r"""(?:\s*)     # Find a discard any leading spaces
                                 ([\.\w]*)    # Find the dataset name, possibly with a period in it.
                                 (?:\(.*?\))* # Find an optional parenthetical and discard it.
                                 """,test1.group(0),flags=re.M|re.S|re.X)
            if test2:
                self.outdatasets=[x for x in test2 if x != '']
            else:
                self.outdatasets=['(NONE)']
        else:
            self.outdatasets=['(NONE)']

            
    def parseDataChunk(thisChunk):
        # OLD CODE
        outset = re.search(r'(?<=set )\s*(?P<ds>(\w|\.)+)',thisChunk,flags=re.MULTILINE)
        if outset:
            outds=outset.group('ds')
        else:
            outds="(FAIL)"
        inset = re.search(r'\s*(?P<ds>[\w\.]+)',thisChunk,flags=re.MULTILINE)
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


        
