'''
@author: matt

There are K pegs. Each peg can hold discs in decreasing order of radius when
looked from bottom to top of the peg. There are N discs which have radius 1 to
N; Given the initial configuration of the pegs and the final configuration of
the pegs, output the moves required to transform from the initial to final
configuration. You are required to do the transformations in minimal number of
moves.

A move consists of picking the topmost disc of any one of the pegs and placing
it on top of anyother peg. At anypoint of time, the decreasing radius property
of all the pegs must be maintained.

Constraints:
1 <= N <= 8
3 <= K <= 5


Input Format:
N K

2nd line contains N integers.

Each integer in the second line is in the range 1 to K where the i-th integer
denotes the peg to which disc of radius i is present in the initial
configuration.

3rd line denotes the final configuration in a format similar  to the initial configuration.


Output Format:

The first line contains M - The minimal number of moves required to complete the transformation. 

The following M lines describe a move, by a peg number to pick from and a peg number to place on.

If there are more than one solutions, it's sufficient to output any one of them.
You can assume, there is always a solution with less than 7 moves and the
initial confirguration will not be same as the final one.

Sample Input #00:

 
2 3
1 1
2 2

Sample Output #00:
 
3
1 3
1 2
3 2


Sample Input #01:

6 4
4 2 4 3 1 1
1 1 1 1 1 1

Sample Output #01:

5
3 1
4 3
4 1
2 1
3 1

NOTE: You need to write the full code taking all inputs are from stdin and outputs to stdout 
If you are using "Java", the classname is "Solution"

'''
from copy import deepcopy
from collections import deque

class Move():
    fromPeg = None
    toPeg = None
    
    def __init__(self, fromPeg, toPeg):
        self.fromPeg = fromPeg
        self.toPeg = toPeg
        
    def __str__(self):
        return "%s %s" % (self.fromPeg, self.toPeg)
        
class GameState():
    _state = []
    _hash = None
    level = 0
    parent = None
    move = None
    
    def __init__(self, stateAsStr=None, numPegs=None, numDiscs=None):
        if stateAsStr and numPegs and numDiscs:
            # create empty number of pegs
            self._state = [[] for i in range(numPegs)]
            for disc_index, peg in enumerate(stateAsStr.split(" ")):
                self._state[int(peg) - 1].insert(0, disc_index+1)
                
    def __str__(self):
        return str(self._state)
        
    def hash(self):
        if self._hash is not None:
            return self._hash
        self._hash = 0
        for peg_index, peg in enumerate(self._state):
            for disc in peg:
                chunk = (peg_index+1) << ((disc - 1) * 4)
                self._hash = self._hash + chunk
        return self._hash
    
    def moves(self):
        moves = []
        for peg_index, peg in enumerate(self._state):
            if not peg:
                # skip empty pegs
                continue
            disc = peg[-1]
            for peg_to_index, peg2 in enumerate(self._state):
                if peg_to_index == peg_index:
                    continue # skip same peg
                disc_to = None
                if peg2:
                    # dest peg has a disc
                    disc_to = peg2[-1]
                # now see if the peg has no disc
                # or a disc that is bigger
                if not disc_to or disc_to > disc:
                    move = Move(peg_index+1, peg_to_index+1)
                    moves.append(move)
        return moves
    
    def applyMove(self, move):
        # pop disc from peg to peg
        fromPeg = self._state[move.fromPeg-1]
        disc = fromPeg.pop()
        toPeg = self._state[move.toPeg-1]
        toPeg.append(disc)
        self.move = move
        
    def __eq__(self, state):
        return self.hash() == state.hash()
    
    def copy(self):
        newState = GameState()
        newState._state = deepcopy(self._state)
        return newState
        
    def moveHistory(self):
        # following parent prints the list of moves to get to this state
        moves = []
        currState = self
        while currState and currState.move:
            moves.append(currState.move)
            currState = currState.parent
        moves.reverse()
        return moves
                
    
class SetOfStates():
    _store = {}
    
    def add(self, state):
        key = state.hash()
        self._store[key] = state
        
    def __contains__(self, state):
        key = state.hash()
        return key in self._store
    
MAX_LEVEL = 7

def search(initialState, desiredState):
    seenStates = SetOfStates()
    q = deque()
    q.append(initialState)
    while q:
        currState = q.popleft()
        seenStates.add(currState)
        listOfMoves = currState.moves()
        for move in listOfMoves:
            newState = currState.copy()
            newState.level = currState.level + 1
            newState.parent = currState
            newState.applyMove(move)
            if newState in seenStates or newState.level > MAX_LEVEL:
                # skip seen states or states more than max
                continue
            if newState == desiredState:
                return newState.moveHistory()
            q.append(newState)
    return None

def printMoves(state):
    
    print len(moves)
    for move in moves:
        print "%s %s" % (move.fromPeg, move.toPeg)
    return moves

import unittest


class Test(unittest.TestCase):


    def testSample00(self):
        numPegs = 3
        numDiscs = 2
        current = "1 1"
        desired = "2 2"
        initialState = GameState(current, numPegs, numDiscs)
        desiredState = GameState(desired, numPegs, numDiscs)
        moves = search(initialState, desiredState)
        self.assertEquals(3, len(moves))
        self.assertEquals(moves[0].fromPeg, 1)
        self.assertEquals(moves[0].toPeg, 3)
        self.assertEquals(moves[1].fromPeg, 1)
        self.assertEquals(moves[1].toPeg, 2)
        self.assertEquals(moves[2].fromPeg, 3)
        self.assertEquals(moves[2].toPeg, 2)
        
    def testSample01(self):
        numPegs = 4
        numDiscs = 6
        current = "4 2 4 3 1 1"
        desired = "1 1 1 1 1 1"
        initialState = GameState(current, numPegs, numDiscs)
        desiredState = GameState(desired, numPegs, numDiscs)
        moves = search(initialState, desiredState)
        self.assertEquals(5, len(moves))
        


if __name__ == "__main__":
    # read STDIN
    import sys
    data = sys.stdin.readlines()
    (numDiscs, numPegs) = data[0].split(" ")
    numPegs = int(numPegs)
    numDiscs = int(numDiscs)
    initialState = GameState(data[1], numPegs, numDiscs)
    desiredState = GameState(data[2], numPegs, numDiscs)
    moves = search(initialState, desiredState)
    print len(moves)
    for move in moves:
        print "%s %s" % (move.fromPeg, move.toPeg)
