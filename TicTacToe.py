import Environment
import Grid
from Agent import *

#First initialize players and their respective chunks

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
'''
R1a= Chunk3 (P2,"R1a","s1","member_of","Row1")
R1b= Chunk3 (P2,"R1b","s2","member_of","Row1")
R1c= Chunk3 (P2,"R1c","s3","member_of","Row1")
R1= Chunk3 (P2,"Row1","is_a","Row")
(etc.)
'''

#First create tic-tac-toe environment
TTT= Environment.Environment(P1, P2)


#Create chunks representing the board, add them to chunk display list.
s1 = Chunk3(TTT,'s1', '_', 1, (1, 1), 0.0); TTT.chunk_display.append(s1)
s2 = Chunk3(TTT,'s2', '_', 2, (2, 1), 0.0); TTT.chunk_display.append(s2)
s3 = Chunk3(TTT,'s3', '_', 3, (3, 1), 0.0); TTT.chunk_display.append(s3)
s4 = Chunk3(TTT,'s4', '_', 4, (1, 2), 0.0); TTT.chunk_display.append(s4)
s5 = Chunk3(TTT,'s5', '_', 5, (2, 2), 0.0); TTT.chunk_display.append(s5)
s6 = Chunk3(TTT,'s6', '_', 6, (3, 2), 0.0); TTT.chunk_display.append(s6)
s7 = Chunk3(TTT,'s7', '_', 7, (1, 3), 0.0); TTT.chunk_display.append(s7)
s8 = Chunk3(TTT,'s8', '_', 8, (2, 3), 0.0); TTT.chunk_display.append(s8)
s9 = Chunk3(TTT,'s9', '_', 9, (3, 3), 0.0); TTT.chunk_display.append(s9)


#Add display grid for easy viewing.
TTT.grid = Grid.Grid(3, 3, raw_chunks = TTT.chunk_display, display_attr = 'thingX')

#First some operators
BECOMES = '='
IS = '=='
ADDED2 = '{0}.append({1})'
nothing = '""'
empty = '[]'
zero = '0'
one = '1'


#Some aliases for easier production definitions.
goal='self.agent.goal'
subgoal='self.agent.subgoal'
focus='self.agent.focus'
view = 'self.agent.view'
is_string = 'isinstance(self.agent.focus[-1:],str)'
check_rows = '"check rows"'
subfocus = 'self.agent.sub_focus'


move = 'self.agent.effector'

start = '"start"'
assess = '"assess"'
wait = '"wait"'

check_rows = '"check rows"'
find_blank = '"find blank"'

#Some more sophisticated functions.  Note that searches all take zero as the list of objects to search in.  The search space.
search2 = 'self.agent.search({0}, {1})'
search3 = 'self.agent.search({0}, {1}, {2})'
search4 = 'self.agent.search({0}, {1}, {2}, {3})'
target1 = 'self.agent.returnID({0})'
modify2 = 'self.e.write({0}, {1})'
random1 = 'self.agent.random_choose({0})'
more_than_zero = 'len({0}) > 0'
assess1 = 'self.agent.assess({0})'
strip2 = 'self.agent.stripChunk({0},{1})'


quantify1 = 'len({0})'
say1    = 'print {0}' 
world = 'self.e.memory'
memory = 'self.agent.memory'

agent1 = 'self.e.Agent1'
agent2 = 'self.e.Agent2'
agent1goal = 'self.e.Agent1.goal'
agent2goal = 'self.e.Agent2.goal'


end = 'self.e.running = False'

#And now actual productions.  First player 1.
x_01  =  Production(P1,   TTT,    [goal + IS + start], [goal + BECOMES + assess, subgoal + BECOMES + nothing])
x_08  =  Production(P1,   TTT,    [goal + IS + wait],  [goal + BECOMES + wait])

#Look for any blank and randomly choose it.
x_02  =  Production(P1,   TTT,    [goal + IS + assess,  subgoal + IS + nothing],    [subgoal + BECOMES + find_blank ])
x_03  =  Production(P1,   TTT,    [goal + IS + assess,  subgoal + IS + find_blank],  [focus + BECOMES + search2.format(world, '"_"'), subgoal + BECOMES + '"quantify"' ])
x_04  =  Production(P1,   TTT,    [goal + IS + assess,  subgoal + IS + '"quantify"', more_than_zero.format(focus)],
                                                                                        [say1.format(quantify1.format(focus)),
                                                                                        subgoal + BECOMES + '"randomly choose"'])

#If its supposed to randomly choose, put your mark there.                                                                                        
x_05  =  Production(P1,   TTT,    [goal + IS + assess,  subgoal + IS + '"randomly choose"'], 
                                    [subfocus + BECOMES + random1.format(focus),
                                    move + BECOMES + target1.format(subfocus),
                                    modify2.format(move, agent1),
                                    subfocus + BECOMES + empty,
                                    goal + BECOMES + wait,
                                    agent2goal + BECOMES + start])


                  
#Now player 2
o_01  =  Production(P2,   TTT,    [goal + IS + start], [goal + BECOMES + assess, subgoal + BECOMES + nothing])
o_08  =  Production(P2,   TTT,    [goal + IS + wait],  [goal + BECOMES + wait])

#Look for any blank and randomly choose it.
o_02  =  Production(P2,   TTT,    [goal + IS + assess,  subgoal + IS + nothing],    [subgoal + BECOMES + find_blank ])
o_03  =  Production(P2,   TTT,    [goal + IS + assess,  subgoal + IS + find_blank],  [focus + BECOMES + search2.format(world, '"_"'), subgoal + BECOMES + '"quantify"' ])
o_04  =  Production(P2,   TTT,    [goal + IS + assess,  subgoal + IS + '"quantify"', more_than_zero.format(focus)],
                                                                                        [say1.format(quantify1.format(focus)),
                                                                                        subgoal + BECOMES + '"methodically choose"'])

#If its supposed to methodically choose, put your mark there.                                                                                        
o_05  =  Production(P2,   TTT,    [goal + IS + assess,  subgoal + IS + '"methodically choose"'],
                                    [subfocus + BECOMES + strip2.format(focus, "'ID'"),
                                    move + BECOMES + assess1.format(subfocus),
                                    modify2.format(move, agent2),
                                    
                                    #Now clear things
                                    goal + BECOMES + wait,
                                    agent1goal + BECOMES + start])
                                    

#Check to see if game is over.
o_06  =  Production(P2,   TTT,    [ search3.format(world, '"_"', '"s"') + IS + empty ],    [ end ])


#Now, start production.
TTT.startGame(n=100)