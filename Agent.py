import random
from Chunks import *
from Productions import *

class Agent():
    '''I am any entity that can play Tic-Tac-Toe.  I contain the production system to play a basic computer opponent of Tic Tac Toe'''
    def __init__(self, ID, winList=[], focus_buffer=[], view=[]):
        self.ID = ID
        self.focus= focus_buffer
        self.my_move = 0
        self.view = view
        self.effector = ""
        self.goal=""
        self.subgoal=""
        self.memory=[]
        self.productionList=[]
    
    def look(self):
        '''I take in Chunks from self.view and convert to visual info and put them in the focus_buffer'''
        self.focus_buffer = []
        
        for each_chunk in self.view:
            self.focus_buffer.append(each_chunk.contents)
            
    def lookForSpace(self):
        '''I return a list of all empty spaces on the board.'''
        
        self.look()
        
        empty_spaces = []
        for square_location, square_contents in enumerate(self.focus_buffer):
            if ' ' in square_contents:
                empty_spaces.append(square_location)
            else:
                pass
        
        return empty_spaces
        
    def random_choose(self, object_list):
        '''I return a random choice from all possible choices in a list.  Hopefully more useful functions will replace me.
        '''
        if len(object_list) == 0:
            return None
        else:
            choice = random.choice(object_list)        
            return choice

    def returnSqr(self,ID=None,att=None,Y=None,num="all"):
        '''returns the first chunk matching the description.
        ID,att,and Y are strings matching parts of Chunk3
        num is either 'first' or 'all' telling the function
        whether to exit upon finding 1 entry. 
        ex. P1.returnSqr(None,None,"_")
        >>> returns all empty spaces.
        '''
        returnList=[]
        for item in self.memory:
            if((item.thingX==ID) or (ID==None))and((item.relation==att)or(att==None))and((item.thingY==Y)or(Y==None)):
                returnList.append(item)
            elif num=="first" and len(returnList)==1:
                return returnList[0]
            else:
                pass
                
        if len(returnList)==1:
            return returnList[0]
        else:
            return returnList

    def returnMissing(self,ID=None,att=None,Y=None,num="all"):
        '''runs returnSqr and returns anID or thingY or a list of matching chunks.
        num is either "first" or "all" in regards to how many chunks are returned'''
        x= self.returnSqr(ID,att,Y,num)
        if isinstance(x,Chunk):
            if ID==None:
                return x.thingX
            elif Y==None:
                return x.thingY
        elif isinstance(x,list):
            returnList=[]
            if ID==None:
                for item in x:
                    returnList.append(item.thingX)
            elif Y==None:
                for item in x:
                    returnList.append(item.thingY)
            return returnList
        return x

    def returnLine(self,anID,att):
        '''anID is a string representing a square (ex."s1")
        att is a string "Diagonal","Row",or "Column"
        '''
        returnList=[]
        x=self.returnMissing(None,"is_a",att,"all")
        #!!!!I could make two iterations (for row in x: for s in row:) but I know there's a cleaner way.
        for line in x:
            for s in line:
                if s==anID:
                    returnList.append(line)
        return returnList
    
    def returnRows(self,anID):
        '''returns a list of lists, each one a single row the space is linked to.
        ex. P1.rR("s1")
        >>>[[1,2,3],[1,5,9],[1,4,7]]'''
        returnList=[]
        
        x=self.returnLine(anID,"Row")
        #returns a list of all thingX's from chunks ending in "Row" (i.e. all 3 rows)
        returnList+=x
        y=self.returnLine(anID,"Column")
        returnList+=y
        if self.returnMissing(anID,"has_type")=="corner" or self.returnMissing(anID,"has_type")=="center":
            z=self.returnLine(anID,"Diagonal")
            returnList+=z
        return returnList
            

    def utility(self,anID):
        '''gives the utility of a single space given the rules of utility provided by Ben W.
        returns an integer
        '''
        utility=0
        a=self.returnRows(anID)
        for line in a:
            blankCount=0
            selfCount=0
            oppCount=0
            for space in line:
                x=self.returnMissing(space,"has_$")
                if x=="_":
                    blankCount+=1
                elif x==self.ID:
                    selfCount+=1
                else:
                    oppCount+=1
            if blankCount==2 and selfCount==1:
                utility+=4
            elif blankCount==3:
                utility+=3
            elif blankCount==2 and oppCount==1:
                utility+=2
            elif selfCount>=1 and oppCount>=1:
                utility+=1
            elif selfCount==2 and blankCount==1:
                utility+=100
            elif oppCount==2 and blankCount==1:
                utility+=50
        return utility

    def assess(self,aList):
        '''Returns the most optimal value for the board'''

        print aList
        '''aList is a list of ID strings(ex."s1")'''
        best=None
        utility=0
        for item in aList:
            x=self.utility(item)
            if best==None:
                best=item
                utility=x
            else:
                if utility<x:
                    best=item
                    utility=x
                else:
                    pass
        print "Best", best
        return best

    def CheckWinLoss(self):
        '''x is a list of string ("s1"etc.) that have agent's sign.
        y is a list of all rows.
        '''
        x=self.returnMissing(None,"has_$",self.ID)
        y= []
        y+=self.returnMissing(None,None,"Row")
        y+=self.returnMissing(None,None,"Column")
        y+=self.returnMissing(None,None,"Diagonal")
        for line in y:
            if len([s for s in x if s in line])==3:
                self.goal= "End"
                print "Game Over. Player "+self.ID+" Wins."
                break
                #return True
        return False
        
    def searchByAttribute(self, chunkList, attribute, attributeContains):
        '''returns a list of chunks matching specified arguments'''
        returnList = []
        
        for i in chunkList:
            #print i
            attribute_contents = getattr(i, attribute)
            try:
                if str(attributeContains) in str(attribute_contents):
                    #print attributeContains, "MATCHes to", attribute_contents
                    returnList.append(i)
                    
                else:
                    pass
                    #print attribute_contents, "No match to", attributeContains
            except:
                pass
                #print "not matching attribute"
            
            #     print attributeType, attributeContains, "Not found"
            #         
        return returnList
    
    def stripChunk(self, chunkList, attribute):
        '''returns a list of chunks' attributes'''
        returnList = []
        
        for chunk in chunkList:
            attr = getattr(chunk, attribute)
            returnList.append(attr)
            
        return returnList
        
        
    def search(self, chunkList, *args):
        '''Filters out a list of chunks by arguments.  Takes in a list of chunks, and returns the ones with attributes
        containing **all** the arguments.'''
        
        returnList = []
        matched = []
        arguments = set(args)
        
        for chunk in chunkList:
            all_attributes = dir(chunk)
            matched = []
            
            for attributes in all_attributes:
                candidate = getattr(chunk, attributes)
                
                for a in args:
                    if (str(a) in str(candidate)) and ("__" not in str(candidate)): #We want to filter out the __builtin__ stuff. 
                        matched.append(a)
                    else:
                        pass
            
            matched = set(matched)
            
            if matched == arguments:
                #print "THEY MATCH"
                returnList.append(chunk)
            else:
                #print "NO MATCH"
                pass
                    
                    
        return returnList
        
    def returnID(self, thatChunk):
        '''Returns ID of nth chunk in a list'''
        
        print getattr(thatChunk, 'ID')                    
        return str(getattr(thatChunk, 'ID'))
        
            
    def SortProductions(self):
        '''Evaluates the truth conditions of all agent productions'''
        
        if self.goal != "End":
            high=0
            FireNext=None
            for item in self.productionList:
                if item.askLS()==True and FireNext!=None:
                    if len(item.LS)>len(FireNext.LS):
                        high=int(item.askLS())
                        FireNext=item
                elif item.askLS()==True and FireNext==None:
                    FireNext=item
                else:
                    pass
            if FireNext!=None:
                FireNext.fire()
            else:
                return "Stop!"
        else:
            return

    def alterChunk(self,ID,newInput):
        '''finds an existing 'has_$' chunk and overrides it with new data'''
        for idea in self.memory:
            if idea.thingX==ID and idea.relation=="has_$":
                idea.thingY=newInput
                return
                
P1=Agent("x")

s1Loc= Chunk3 (P1,"s1@","s1","has_loc",(1,1))
s2Loc= Chunk3 (P1,"s1@","s2","has_loc",(1,2))
s3Loc= Chunk3 (P1,"s1@","s3","has_loc",(1,3))
s4Loc= Chunk3 (P1,"s1@","s4","has_loc",(2,1))
s5Loc= Chunk3 (P1,"s1@","s5","has_loc",(2,2))
s6Loc= Chunk3 (P1,"s1@","s6","has_loc",(2,3))
s7Loc= Chunk3 (P1,"s1@","s7","has_loc",(3,1))
s8Loc= Chunk3 (P1,"s1@","s8","has_loc",(3,2))
s9Loc= Chunk3 (P1,"s1@","s9","has_loc",(3,3))
s1S= Chunk3 (P1,"s1S","s1","has_$","_")
s2S= Chunk3 (P1,"s2S","s2","has_$","_")
s3S= Chunk3 (P1,"s3S","s3","has_$","_")
s4S= Chunk3 (P1,"s4S","s4","has_$","_")
s5S= Chunk3 (P1,"s5S","s5","has_$","_")
s6S= Chunk3 (P1,"s6S","s6","has_$","_")
s7S= Chunk3 (P1,"s7S","s7","has_$","_")
s8S= Chunk3 (P1,"s8S","s8","has_$","_")
s9S= Chunk3 (P1,"s9S","s9","has_$","_")
s1R= Chunk3 (P1,"s1R","s1","has_type","corner")
s2R= Chunk3 (P1,"s2R","s2","has_type","edge")
s3R= Chunk3 (P1,"s3R","s3","has_type","corner")
s4R= Chunk3 (P1,"s4R","s4","has_type","edge")
s5R= Chunk3 (P1,"s5R","s5","has_type","center")
s6R= Chunk3 (P1,"s6R","s6","has_type","edge")
s7R= Chunk3 (P1,"s7R","s7","has_type","corner")
s8R= Chunk3 (P1,"s8R","s8","has_type","edge")
R123= Chunk3 (P1,"R123",["s1","s2","s3"],"is_a","Row")
R456= Chunk3 (P1,"R456",["s4","s5","s6"],"is_a","Row")
R789= Chunk3 (P1,"R789",["s7","s8","s9"],"is_a","Row")
C147= Chunk3 (P1,"C147",["s1","s4","s7"],"is_a","Column")
C258= Chunk3 (P1,"C258",["s2","s5","s8"],"is_a","Column")
C369= Chunk3 (P1,"C369",["s3","s6","s9"],"is_a","Column")
D159= Chunk3 (P1,"D159",["s1","s5","s9"],"is_a","Diagonal")
D357= Chunk3 (P1,"D357",["s3","s5","s7"],"is_a","Diagonal")

P2=Agent("o")
s1Loc= Chunk3 (P2,"s1@","s1","has_loc",(1,1))
s2Loc= Chunk3 (P2,"s1@","s2","has_loc",(1,2))
s3Loc= Chunk3 (P2,"s1@","s3","has_loc",(1,3))
s4Loc= Chunk3 (P2,"s1@","s4","has_loc",(2,1))
s5Loc= Chunk3 (P2,"s1@","s5","has_loc",(2,2))
s6Loc= Chunk3 (P2,"s1@","s6","has_loc",(2,3))
s7Loc= Chunk3 (P2,"s1@","s7","has_loc",(3,1))
s8Loc= Chunk3 (P2,"s1@","s8","has_loc",(3,2))
s9Loc= Chunk3 (P2,"s1@","s9","has_loc",(3,3))
s1S= Chunk3 (P2,"s1S","s1","has_$","_")
s2S= Chunk3 (P2,"s2S","s2","has_$","_")
s3S= Chunk3 (P2,"s3S","s3","has_$","_")
s4S= Chunk3 (P2,"s4S","s4","has_$","_")
s5S= Chunk3 (P2,"s5S","s5","has_$","_")
s6S= Chunk3 (P2,"s6S","s6","has_$","_")
s7S= Chunk3 (P2,"s7S","s7","has_$","_")
s8S= Chunk3 (P2,"s8S","s8","has_$","_")
s9S= Chunk3 (P2,"s9S","s9","has_$","_")
s1R= Chunk3 (P2,"s1R","s1","has_type","corner")
s2R= Chunk3 (P2,"s2R","s2","has_type","edge")
s3R= Chunk3 (P2,"s3R","s3","has_type","corner")
s4R= Chunk3 (P2,"s4R","s4","has_type","edge")
s5R= Chunk3 (P2,"s5R","s5","has_type","center")
s6R= Chunk3 (P2,"s6R","s6","has_type","edge")
s7R= Chunk3 (P2,"s7R","s7","has_type","corner")
s8R= Chunk3 (P2,"s8R","s8","has_type","edge")
s9R= Chunk3 (P2,"s9R","s9","has_type","corner")
R123= Chunk3 (P2,"R123",["s1","s2","s3"],"is_a","Row")
R456= Chunk3 (P2,"R456",["s4","s5","s6"],"is_a","Row")
R789= Chunk3 (P2,"R789",["s7","s8","s9"],"is_a","Row")
C147= Chunk3 (P2,"C147",["s1","s4","s7"],"is_a","Column")
C258= Chunk3 (P2,"C258",["s2","s5","s8"],"is_a","Column")
C369= Chunk3 (P2,"C369",["s3","s6","s9"],"is_a","Column")
D159= Chunk3 (P2,"D159",["s1","s5","s9"],"is_a","Diagonal")
D357= Chunk3 (P2,"D357",["s3","s5","s7"],"is_a","Diagonal")
