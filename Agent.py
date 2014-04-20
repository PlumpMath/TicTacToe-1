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
        
    def random_choose(self):
        '''I return a random choice from all possible choices.  Hopefully more useful functions will replace me.
        '''
        all_choices = self.lookForSpace()
        if len(all_choices) == 0:
            return None
        else:
            choices = random.choice(all_choices)        
            return choices

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
                
        #if len(returnList)==1:
            #return returnList[0]
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
            
    def SortProductions(self):
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

    def alterChunk(self,ID,newInput):
        #finds an existing 'has_$' chunk and overrides it with new data
        for idea in self.memory:
            if idea.thingX==ID and idea.relation=="has_$":
                idea.thingY=newInput
                return
