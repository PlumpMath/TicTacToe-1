class Grid:
    '''Draws text-grids based on requested width, height, and list contents.  Lists should be chunks, but can 
    be plain lists by keyword argument, like : chunks='list'.
    
    Example Usage1: x = Grid(3, 3, chunk1_list)
    Example Usage2: x = Grid(3, 3, chunks = regularList).'''
    
    def __init__(self, width=0, height=0, raw_chunks=None, chunks = [], current_grid = '', history = [], display_attr = ''):
        #position should be [x,y]
        self.width = width
        self.height = height
        self.raw_chunks = raw_chunks
        self.chunks = chunks
        self.current_grid = current_grid
        self.history = history
        self.display_attr = display_attr
                
        #Put the productions' 'raw' chunks' contents attributes into its own list.
        if self.raw_chunks:
            self.update(self.raw_chunks)
        else:
            pass
                    
    def make_row(self, slice_start=0):
        '''Makes a single row based on width attribute.'''
                
        squares = '|'
        start = self.width * slice_start
        end = start + self.width
        
        chunk_slice = self.chunks[start : end]
        
        for chunks in chunk_slice:
            chunks = str(chunks)
            
            if len(chunks) > 1:
                squares += "%s |" % (chunks)
            else:
                squares += " %s |" % (chunks)
            
        return squares
            
    def update(self, raw_chunks = None):
        '''(re)generates a grid from width and height attributes, and potentially new chunk attributes inside.
        
        example usage1: grid_instance.update()
        example usage2: grid_instance.update(raw_chunks)
        
        '''
        
        #If there's a new list of chunks as an argument, update those now.  Otherwise just skip.
        #chunks.
        if raw_chunks:
            self.chunks = []
        
            for chunks in self.raw_chunks:
                attr = getattr(chunks, self.display_attr)
                self.chunks.append(attr)
            else:
                pass
        
        #Make some lists for row dimensions
        row_list = []
        row_lengths = []
        
        #Get all the rows, and combine them in a list based on the height attribute.
        for row in range(0, self.height):
            row_list.append(self.make_row(row))
            row_lengths.append(len(self.make_row(row)))
            
        #Make a 'grid' string to put all of the above into.  Also find the longest row out of all
        #the rows.
        self.current_grid = ''
        max_row_length = max(row_lengths)
        
        horizontal_divider = "-" * max_row_length
        
        #Put each row into its own line, and add them to a string.
        for row in row_list:
            self.current_grid += "\n" + horizontal_divider
            self.current_grid += "\n" + row
            
        #Finally, add the bottom bit
        self.current_grid += "\n" + horizontal_divider
        
        #Finally, update the history
        self.history.append(self.current_grid)
                
    def show_current(self):
        '''Just draws the existing grid in memory.'''
        print self.current_grid
        
    def show_history(self, snapshots=None):
        '''Prints all states of this instance of the grid, ordered first to last without argument, and 
        last to first with argument.
        
        example1: grid_instance.print_history()  << prints all
        example2: grid_instance.print_history(3) << prints last 3 states.'''
        
        print "Board history:"
        
        if snapshots:
            history = reversed(self.history[:snapshots])
            for number, snap in enumerate(history):
                print "%sth LAST STEP:" % (number)
                print snap 
        else:
            for number, snap in enumerate(self.history):
                print "STEP %s:" % (number)
                print snap

       
