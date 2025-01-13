from collections import deque
from Helper import helper, node
import heapq

class astar():
    def __init__(self, fileText):

        self.finalGoal =    [[1, 2, 3],
                             [8, 0, 4],
                             [7, 6, 5]]

        self.helper = helper()
        self.start = self.helper.convertTo2DArray(fileText)             #2d array


        self.openHeap = []                 #3 state
        heapq.heapify(self.openHeap)
        self.close = {}
        self.path = 0
        self.expand = 0

    def calculate_h(self, currState, goalState):                    #h()
        h = 0
        currState = currState.getState()
        for r in range(len(currState)):
            for c in range(len(currState[0])):
                if (currState[r][c] != goalState[r][c]):
                    h += 1
        return h
    
    def calculate_f(self, currState, goalState):                    #f()
        return self.calculate_h(currState, goalState) + currState.getDepth()
     
    def solveWithAStar(self):
        target = self.finalGoal
        start = node(self.start, 0, 0)
        start.f = self.calculate_f(start, self.finalGoal)
        # Append the start node and its parent to the openHeap
        heapq.heappush(self.openHeap, (start.f, start, None))

        while len(self.openHeap) > 0:                   # == while len(self.openQueue) > 0
            print(self.openHeap)
            f_val, revState, parent = heapq.heappop(self.openHeap) # revState of type Node
            hashRev = self.helper.hashState(revState.getState())
          
            self.close[hashRev] = (revState, parent)

            if (self.calculate_h(revState, target) == 0):
                return 1

            adjList = revState.generateAdjNode(revState.getState())

            for adj in adjList:
                adj.f = self.calculate_f(adj, target)

            for adj in adjList:
                hashAdj = self.helper.hashState(adj.getState())
                if hashAdj not in self.close:
                    self.close[hashAdj] = ()  # discover
                    print(adj.f)
                    heapq.heappush(self.openHeap, (adj.f, adj, revState))
                    self.expand += 1
        return 0
    
    def getSolution(self):
        result = self.solveWithAStar()
        if not result:  #result == 0
            print('leu leu')
            return

        ans = []
        hashState = self.helper.hashState(self.finalGoal)
        while self.close[hashState][1] != None:
            ans.append(self.close[hashState][0].getState())
            hashState = self.helper.hashState(self.close[hashState][1].getState())
            self.path += 1
        ans.append(self.start)
        print("--------Initial state---------")
        self.helper.printMatrix(ans[len(ans)-1])

        for i in range(len(ans)-2 , -1, -1):
            print(f"---------Move {len(ans)-i -1}-------------")
            self.helper.printMatrix(ans[i])
        print("Total number of path:", self.path)
        print("Total number of node expand: ", self.expand)


