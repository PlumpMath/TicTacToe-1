from Grid import *

class Environment():

    def __init__(self,Agent1,Agent2, chunk_display=[]):
        self.Agent1 = Agent1
        self.Agent2 = Agent2
        self.memory=[]
        self.chunk_display = chunk_display
        self.running = True
        
        self.grid = None
        
    def write(self,c,Agent):
        '''write the agent ID on a space c
        c is a string (ex. "s3")
        Agent is an Agent instance who is claiming the square
        '''
        for item in self.memory:
            if item.ID==c:
                item.thingX=Agent.ID
                Agent.focus = []
                Agent.focus.append(c)
        
        self.switchTurns(Agent)
        self.update()
        
    def switchTurns(self, Agent):
        '''Switches which agent is able to play.'''
        if Agent.ID == self.Agent1.ID:
            self.Agent2.goal = "start"
        elif Agent.ID == self.Agent2.ID:
            self.Agent1.goal = "start"

    def startGame(self):
        #This will be the initialization of the game.
        self.Agent1.goal="start"
        self.Agent2.goal="wait"
        count=100
        while count>=0 and (self.Agent1.returnMissing(None,None,"_")!=[]) and self.running == True:
            self.Agent1.SortProductions()
            self.Agent2.SortProductions()
            count-=1
            
        print "End of production"

    def printBoard (self):
        
        if self.grid:
            self.grid.update(self.chunk_display)
            self.grid.show_current()
            
        else:
            pass
                    
    def update(self):
        '''update will change all chunks in agents to match the environment'''
        for item in self.memory:
            self.Agent1.alterChunk(item.ID,item.thingX)
            self.Agent2.alterChunk(item.ID,item.thingX)
        self.printBoard()
        
