
from collections import deque
from Helper import helper


class bfs():
    def __init__(self, fileText):                      #constructor
        self.helper = helper()                         #private
        self.start = self.helper.convertTo2DArray(fileText)                     

        self.openQueue = deque()                       #3 state
        self.openQueue.append((self.start, None))

        self.close = {}
        self.path = 0
        self.expand = 0


        self.finalGoal =    [[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]]

    def solveWithBFS(self):
        target = self.finalGoal
        while self.openQueue:                   # == while len(self.openQueue) > 0
            revState, parent = self.openQueue.popleft()
            hashRev = self.helper.hashState(revState)
            self.close[hashRev] = (revState, parent)
            if revState == target:
                return 1

            adjList = self.helper.generateAdj(revState)
            

            for adj in adjList:
                hashAdj = self.helper.hashState(adj)
                if hashAdj not in self.close:
                    self.close[hashAdj] = ()        #discover
                    self.openQueue.append((adj, revState))
                    self.expand += 1
        return 0

    def getSolution(self):
        result = self.solveWithBFS()
        if not result:  #result == 0
            print(' leu leu')
            return

        ans = []
        hashState = self.helper.hashState(self.finalGoal)
        while self.close[hashState][1] != None:
            ans.append(self.close[hashState][0])
            hashState = self.helper.hashState(self.close[hashState][1])
            self.path += 1
        ans.append(self.start)
        print("--------Initial state---------")
        self.helper.printMatrix(ans[len(ans)-1])

        for i in range(len(ans)-2 , -1, -1):
            print(f"---------Move {len(ans)-i -1}-------------")
            self.helper.printMatrix(ans[i])
        print("Total number of path:", self.path)
        print("Total number of node expand: ", self.expand)