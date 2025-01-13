
from copy import deepcopy

class helper():
    ### Movement: 
    # (-1, 0): Up   
    # (0, -1): Left   
    # (1, 0): Down
    # (0, 1): Right
    # def __init__(self):
    ROW_MOVE = [-1, 0, 1, 0]
    COLUMN_MOVE = [0, -1, 0, 1]
    SIZE = 3

    def convertTo2DArray(self, textFile):        #declare type
        row = textFile.split('\n')
        twoDArr = [r.split(' ') for r in row]
        twoDArr2 = [[int(i) for i in row] for row in twoDArr]
        return twoDArr2
    
    def findZero(self, currState):
        for r in range(len(currState)):
            for c in range(len(currState[0])):
                if (currState[r][c] == 0):
                    return (r, c)  


    def swap(self, currState, r1, c1, r2, c2):
        stateCopy = deepcopy(currState)
        stateCopy[r1][c1] = currState[r2][c2]
        stateCopy[r2][c2] = currState[r1][c1]

        return stateCopy

    def generateAdj(self, currState):
        cur0Row, cur0Col = self.findZero(currState)
        ans = []
        for i in range(len(self.ROW_MOVE)):
            new0Row, new0Col = cur0Row + self.ROW_MOVE[i], cur0Col + self.COLUMN_MOVE[i]
            if (new0Row >= 0) and (new0Row < self.SIZE) and (new0Col >= 0) and (new0Col < self.SIZE):
                ans.append(self.swap(currState, cur0Row, cur0Col, new0Row, new0Col))
        return ans
    
    def hashState(self, currState):
        ans = []
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                ans.append(str(currState[r][c]))
        return ''.join(ans)

    def printMatrix(self, matr):
        for row in matr:
            print(row)
        print()

class node():
    def __init__(self, state, depth, f):
        self.state = state
        self.depth = depth
        self.f = f

    def getState(self):
        return self.state
    
    def getDepth(self):
        return self.depth
    
    def getF(self):
        return self.f

    def __lt__(self, other):
        return sum(self.state[0]) < sum(other.state[0])

    def generateAdjNode(self, currState):
        curr0Row, curr0Col = self.findZero(currState)
        children = []
        for i in range(len(helper.ROW_MOVE)):
            new0Row, new0Col = curr0Row + helper.ROW_MOVE[i], curr0Col + helper.COLUMN_MOVE[i]
            if (new0Row >= 0) and (new0Row < helper.SIZE) and (new0Col >= 0) and (new0Col < helper.SIZE):
                child = self.swap(currState, curr0Row, curr0Col, new0Row, new0Col)
                childNode = node(child, self.depth + 1, 0)
                children.append(childNode)
        return children  
    
    def findZero(self, currState):
        for r in range(len(currState)):
            for c in range(len(currState[0])):
                if (currState[r][c] == 0):
                    return (r, c)  


    def swap(self, currState, r1, c1, r2, c2):
        stateCopy = deepcopy(currState)
        stateCopy[r1][c1] = currState[r2][c2]
        stateCopy[r2][c2] = currState[r1][c1]

        return stateCopy

    
    
   