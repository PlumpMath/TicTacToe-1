class Chunk:
    "a bit of memory."

    def __init__(self, ID, activation=0.0):
        '''creates a new instance of a chunk

        ID is a string that identifies the chunk, it's identifier
        activation is an optional argument that takes a number between 0.0 and 1.0'''
        self.ID = ID
        self.activation = activation

    def addToActivation(self, addend):
        '''adds the addend to the activation of the chunk and returns the new activation

        addend is a number between -1.0 and 1.0'''
        self.activation = self.activation + addend
        if self.activation > 1.0:
            self.activation = 1.0
        if self.activation < 0.0:
            self.activation = 0
        return self.activation        
# end class Chunk

class Chunk1(Chunk):
    "a bit of memory that has only one part."

    def __init__(self, agent, ID, thingX=0.0, activation=0.0):
        '''creates a new instance of a chunk1, which is a single concept in memory

        ID is a string that identifies it
        thingX is a string that shows what the chunk represents
        activation is a number between 0.0 and 1.0'''
        # indicates whether the chunk is a chunk1 or a chunk3
        self.chunkType = 1
        self.agent = agent
        self.ID = ID
        ## thingX should never be a number. If it is, it's going to be 0.0,
        ##   the default when nothing else is entered.
        ##   When this happens, make thingX equal to the ID.
        if thingX == 0.0:
            self.thingX= self.ID
        else:
            self.thingX = thingX
        self.activation = activation
        agent.memory.append(self)
# end class Chunk1

class Chunk2(Chunk):
    def __init__(self, ID, thingX,thingY, activation=0.0):
        self.chunkType = 2
        self.ID = ID
        self.thingX = thingX
        self.thingY = thingY
        self.activation = activation
        

class Chunk3(Chunk):
    "a bit of memory that has only one part."
    def __init__(self, agent, ID, thingX, relation, thingY, activation=0.0):
        '''creates a new instance of a chunk1, which is a single concept in memory

        agent is the agent who knows the memory in question
        ID is a string that identifies it
        thingX is a string that shows what the chunk represents
        activation is a number between 0.0 and 1.0'''
        # indicates whether the chunk is a chunk1 or a chunk3
        self.chunkType = 3
        self.ID = ID
        self.agent= agent
        self.thingX = thingX
        self.relation = relation
        self.thingY = thingY
        self.activation = activation
        agent.memory.append(self)
        #agent.addChunk1ToMemory(thingX)
        #agent.addChunk1ToMemory(relation)
        #agent.addChunk1ToMemory(thingY)
# end class Chunk3
