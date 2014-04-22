from Grid import *

class Environment():
    '''Environment class for production system.  Requires two agents at the moment.'''

    def __init__(self,Agent1, Agent2, chunk_display=[]):
        self.Agent1 = Agent1
        self.Agent2 = Agent2
        self.memory=[]
        self.chunk_display = chunk_display
        self.running = True
        self.count = 0
        
        self.grid = None
        
    def write(self,c, Agent):
        '''write the agent ID on a space c
        c is a string (ex. "s3")
        Agent is an Agent instance who is claiming the square
        '''
        
        for item in self.memory:
            if item.ID==c:
                item.thingX=Agent.ID
                
                self.printBoard()
                
            else:
                pass

    def startGame(self, n = 50):
        '''This will be the initialization of the game.'''
        
        self.Agent1.goal="start"
        self.Agent2.goal="wait"
        
        while (self.count < n) and (self.running == True):
            self.Agent1.SortProductions()
            self.Agent2.SortProductions()
            
            self.count += 1
            
        else:
            print "End of production"

    def printBoard (self):
        '''displays board every update'''
        
        if self.grid:
            self.grid.update(self.chunk_display)
            self.grid.show_current()
            
        else:
            pass