class Production():
    "a production"

    def __init__(self,agent, Environment, Conditions=[],Action=" "):
        '''creates a new production'''
        self.agent = agent
        self.e=Environment
        self.LS = Conditions
        self.RS = Action
        self.agent.productionList.append(self)
        goal=self.agent.goal
        subgoal=self.agent.subgoal
        focus=self.agent.focus

        
    def fire(self):
        for right_side in self.RS:
            try:
                exec right_side
                print "%s successfully executed production right side: %s" % (self.agent.ID, right_side)
                
            except AttributeError as a:
                print "***\n%s FAILED to execute right side: %s. in %s\n***" % (self.agent.ID, a, right_side)
                
            except IndexError as i:
                print "***\n%s FAILED to execute right side: %s. in %s \n***" % (self.agent.ID, i, right_side)
                
    def askLS(self):
        activation=True
        for item in self.LS:
            exec "b= bool("+item+")"
            if b == False:
                    activation=False
        return activation