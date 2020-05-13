from collections import deque
from operator import attrgetter
from math import pow,sqrt

class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)

    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''

        self.path.clear()
        self.fullPath.clear()

        rows = mazeStr.split()
        self.count_row = len(rows)
        self.count_column = 0
        self.count_nodes = (len(rows[0]) // 2) + 1
        self.count_column = len(rows[0])
        self.nodes = list()
        self.nodes2D = [[0 for j in range(self.count_nodes)] for i in range(self.count_row)]
        count_id = 0

        #fill 1D list with nodes
        for i in range(len(rows)):
            # print(rows[i])
            for j in range(len(rows[i])):
                if rows[i][j] != ',':
                    n = Node(rows[i][j])
                    n.id = count_id
                    if i < self.count_row - 1:
                        n.down = rows[i + 1][j]
                    if i > 0:
                        n.up = rows[i - 1][j]
                    if j < self.count_column - 1:
                        n.right = rows[i][j + 2]
                    if j > 0:
                        n.left = rows[i][j - 2]
                    self.nodes.append(n)
                    count_id += 1

        #get start and end nodes
        for node in self.nodes:
            if node.value == 'S':
                self.startNode = node
            if node.value == 'E':
                self.endNode = node

        #calculate edge dost
        if (edgeCost != None):
            for i in range(len(self.nodes)):
                self.nodes[i].edgeCost = edgeCost[i]

        #copy items from 1D list to 2D list
        for i in range(self.count_row):
            for j in range(self.count_nodes):
                self.nodes2D[i][j] = self.nodes[j + (i * self.count_nodes)]

    def index_2d(self,myList, v):
        for i, x in enumerate(myList):
            if v in x:
                return i, x.index(v)

    def getMin(self, l, sorter):
        m= min(l,key=attrgetter(sorter))
        i=l.index(m)
        l.pop(i)
        return m

    def euclidean(self, x1, y1, x2, y2):
        return sqrt(pow((x1-x2),2)+pow((y1-y2),2))

    def manhattan(self, x1, y1, x2, y2):
        return abs(x1-x2)+abs(y1-y2)

    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        startNode = self.startNode
        endNode = self.endNode
        visited = list([])
        not_visited = deque([startNode])

        while not_visited:
            currentNode = not_visited.popleft()
            i,j=self.index_2d(self.nodes2D,currentNode)
            visited.append(currentNode)
            if currentNode.value == 'E':
                break


            if (currentNode.right == '.' or currentNode.right == 'E') and self.nodes2D[i][j+1] not in visited:
                self.nodes2D[i][j+1].previousNode = currentNode.id
                if self.nodes2D[i][j+1] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i][j+1])


            if (currentNode.left == '.' or currentNode.left == 'E') and self.nodes2D[i][j-1] not in visited:
                self.nodes2D[i][j-1].previousNode = currentNode.id
                if self.nodes2D[i][j-1] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i][j-1])


            if (currentNode.down == '.' or currentNode.down == 'E') and self.nodes2D[i+1][j] not in visited:
                self.nodes2D[i+1][j].previousNode= currentNode.id
                if self.nodes2D[i+1][j] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i+1][j])


            if (currentNode.up == '.' or currentNode.up == 'E') and self.nodes2D[i-1][j] not in visited:
                self.nodes2D[i-1][j].previousNode = currentNode.id
                if self.nodes2D[i-1][j] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i-1][j])




        # fill full path
        for item in visited:
            self.fullPath.append(item.id)
        return self.path, self.fullPath

    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes

        startNode=self.startNode
        endNode=self.endNode
        visited =list([])
        not_visited=deque([startNode])

        while not_visited:
            currentNode = not_visited.pop()
            i, j = self.index_2d(self.nodes2D, currentNode)
            visited.append(currentNode)
            if currentNode.value=='E':
                break



            if (currentNode.up=='.' or currentNode.up=='E' )and self.nodes2D[i-1][j] not in visited :
                self.nodes2D[i-1][j].previousNode=currentNode.id
                if self.nodes2D[i-1][j] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i-1][j])

            if (currentNode.down=='.'or currentNode.down=='E') and self.nodes2D[i+1][j] not in visited :
                self.nodes2D[i+1][j].previousNode=currentNode.id
                if self.nodes2D[i+1][j] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i+1][j])

            if (currentNode.left=='.' or currentNode.left=='E') and self.nodes2D[i][j-1] not in visited:
                self.nodes2D[i][j-1].previousNode = currentNode.id
                if self.nodes2D[i][j-1] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i][j-1])

            if (currentNode.right=='.'or currentNode.right=='E') and self.nodes2D[i][j+1] not in visited :
                self.nodes2D[i][j+1].previousNode=currentNode.id
                if self.nodes2D[i][j+1] not in not_visited:
                    not_visited.appendleft(self.nodes2D[i][j+1])



        #fill path
        temp = endNode
        while temp.id != startNode.id:
            self.path.append(temp.id)
            for i in range(self.count_row):
                for j in range(self.count_nodes):
                    if self.nodes2D[i][j].id == temp.previousNode:
                        temp = self.nodes2D[i][j]
                        break
        self.path.append(startNode.id)
        self.path.reverse()

        #fill full path
        for item in visited:
            self.fullPath.append(item.id)
        return self.path, self.fullPath

    def UCS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        startNode = self.startNode
        endNode = self.endNode
        visited=list([])
        not_visited = list([startNode])

        while not_visited:
            currentNode =self.getMin(not_visited,"edgeCost")
            i, j = self.index_2d(self.nodes2D, currentNode)
            visited.append(currentNode)
            if currentNode.value == 'E':
                break

            if (currentNode.right == '.' or currentNode.right == 'E') and self.nodes2D[i][j+1] not in visited:
                self.nodes2D[i][j+1].previousNode = currentNode.id
                self.nodes2D[i][j+1].edgeCost+=currentNode.edgeCost
                if self.nodes2D[i][j+1] not in not_visited:
                    not_visited.append(self.nodes2D[i][j+1])

            if (currentNode.left == '.' or currentNode.left == 'E') and self.nodes2D[i][j-1] not in visited:
                self.nodes2D[i][j-1].previousNode = currentNode.id
                self.nodes2D[i][j-1].edgeCost+= currentNode.edgeCost
                if self.nodes2D[i][j-1] not in not_visited:
                    not_visited.append(self.nodes2D[i][j-1])

            if (currentNode.up == '.' or currentNode.up == 'E') and self.nodes2D[i-1][j] not in visited:
                self.nodes2D[i-1][j].previousNode = currentNode.id
                self.nodes2D[i-1][j].edgeCost+=currentNode.edgeCost
                if self.nodes2D[i-1][j] not in not_visited:
                    not_visited.append(self.nodes2D[i-1][j])

            if (currentNode.down == '.' or currentNode.down == 'E') and self.nodes2D[i+1][j] not in visited:
                self.nodes2D[i+1][j].previousNode = currentNode.id
                self.nodes2D[i+1][j].edgeCost+=currentNode.edgeCost
                if self.nodes2D[i+1][j] not in not_visited:
                    not_visited.append(self.nodes2D[i+1][j])

        # fill path
        temp = endNode
        while temp.id != startNode.id:
            self.path.append(temp.id)
            for i in range(self.count_row):
                for j in range(self.count_nodes):
                    if self.nodes2D[i][j].id == temp.previousNode:
                        temp = self.nodes2D[i][j]
                        break
        self.path.append(startNode.id)
        self.path.reverse()

        # fill full path
        for item in visited:
            self.fullPath.append(item.id)

        self.totalCost = endNode.edgeCost
        return self.path, self.fullPath, self.totalCost

    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes

        startNode = self.startNode
        endNode = self.endNode
        startNode.gOfN=0

        #Calculate h(N)
        x,y=self.index_2d(self.nodes2D,endNode)
        for i in range(self.count_row):
            for j in range(self.count_nodes):
                self.nodes2D[i][j].hOfN=self.euclidean(i,j,x,y)


        visited = list([])
        not_visited = list([startNode])

        while not_visited:
            currentNode = self.getMin(not_visited, "heuristicFn")
            i, j = self.index_2d(self.nodes2D, currentNode)
            visited.append(currentNode)
            if currentNode.value == 'E':
                break

            if (currentNode.up == '.' or currentNode.up == 'E') and self.nodes2D[i-1][j] not in visited:
                self.nodes2D[i-1][j].previousNode = currentNode.id
                self.nodes2D[i-1][j].gOfN = currentNode.gOfN + self.nodes2D[i-1][j].edgeCost
                self.nodes2D[i-1][j].heuristicFn = self.nodes2D[i-1][j].gOfN + self.nodes2D[i-1][j].hOfN
                if self.nodes2D[i-1][j] not in not_visited:
                    not_visited.append(self.nodes2D[i-1][j])

            if (currentNode.down == '.' or currentNode.down == 'E') and self.nodes2D[i+1][j] not in visited:
                self.nodes2D[i+1][j].previousNode = currentNode.id
                self.nodes2D[i+1][j].gOfN = currentNode.gOfN + self.nodes2D[i+1][j].edgeCost
                self.nodes2D[i+1][j].heuristicFn = self.nodes2D[i+1][j].gOfN + self.nodes2D[i+1][j].hOfN
                if self.nodes2D[i+1][j] not in not_visited:
                    not_visited.append(self.nodes2D[i+1][j])

            if (currentNode.left == '.' or currentNode.left == 'E') and self.nodes2D[i][j-1] not in visited:
                self.nodes2D[i][j-1].previousNode = currentNode.id
                self.nodes2D[i][j-1].gOfN = currentNode.gOfN + self.nodes2D[i][j-1].edgeCost
                self.nodes2D[i][j-1].heuristicFn = self.nodes2D[i][j-1].gOfN + self.nodes2D[i][j-1].hOfN
                if self.nodes2D[i][j-1] not in not_visited:
                    not_visited.append(self.nodes2D[i][j-1])

            if (currentNode.right == '.' or currentNode.right == 'E') and self.nodes2D[i][j+1] not in visited:
                self.nodes2D[i][j+1].previousNode = currentNode.id
                self.nodes2D[i][j+1].gOfN = currentNode.gOfN + self.nodes2D[i][j+1].edgeCost
                self.nodes2D[i][j+1].heuristicFn = self.nodes2D[i][j+1].gOfN + self.nodes2D[i][j+1].hOfN
                if self.nodes2D[i][j+1] not in not_visited:
                    not_visited.append(self.nodes2D[i][j+1])

        # fill path
        temp = endNode
        while temp.id != startNode.id:
            self.path.append(temp.id)
            for i in range(self.count_row):
                for j in range(self.count_nodes):
                    if self.nodes2D[i][j].id == temp.previousNode:
                        temp = self.nodes2D[i][j]
                        break
        self.path.append(startNode.id)
        self.path.reverse()

        # fill full path
        for item in visited:
            self.fullPath.append(item.id)

        self.totalCost = endNode.heuristicFn

        return self.path, self.fullPath, self.totalCost

    def AStarManhattanHeuristic(self):
        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes

        startNode = self.startNode
        endNode = self.endNode
        startNode.edgeCost=0.0

        # Calculate h(N)
        x, y = self.index_2d(self.nodes2D, endNode)
        for i in range(self.count_row):
            for j in range(self.count_nodes):
                self.nodes2D[i][j].hOfN = self.manhattan(i, j, x, y)

        visited = list([])
        not_visited = list([startNode])

        while not_visited:
            currentNode = self.getMin(not_visited, "heuristicFn")
            i, j = self.index_2d(self.nodes2D, currentNode)
            visited.append(currentNode)
            if currentNode.value == 'E':
                break


            if (currentNode.up == '.' or currentNode.up == 'E') and self.nodes2D[i-1][j] not in visited:
                self.nodes2D[i-1][j].previousNode = currentNode.id
                self.nodes2D[i-1][j].edgeCost = currentNode.edgeCost+1
                self.nodes2D[i-1][j].heuristicFn=self.nodes2D[i-1][j].edgeCost+self.nodes2D[i-1][j].hOfN
                if self.nodes2D[i-1][j] not in not_visited:
                    not_visited.append(self.nodes2D[i-1][j])

            if (currentNode.down == '.' or currentNode.down == 'E') and self.nodes2D[i+1][j] not in visited:
                self.nodes2D[i+1][j].previousNode = currentNode.id
                self.nodes2D[i+1][j].edgeCost = currentNode.edgeCost+1
                self.nodes2D[i+1][j].heuristicFn=self.nodes2D[i+1][j].edgeCost+self.nodes2D[i+1][j].hOfN
                if self.nodes2D[i+1][j] not in not_visited:
                    not_visited.append(self.nodes2D[i+1][j])

            if (currentNode.left == '.' or currentNode.left == 'E') and self.nodes2D[i][j - 1] not in visited:
                self.nodes2D[i][j - 1].previousNode = currentNode.id
                self.nodes2D[i][j - 1].edgeCost = currentNode.edgeCost+1
                self.nodes2D[i][j - 1].heuristicFn=self.nodes2D[i][j - 1].edgeCost+self.nodes2D[i][j - 1].hOfN
                if self.nodes2D[i][j - 1] not in not_visited:
                    not_visited.append(self.nodes2D[i][j - 1])

            if (currentNode.right == '.' or currentNode.right == 'E') and self.nodes2D[i][j + 1] not in visited:
                self.nodes2D[i][j + 1].previousNode = currentNode.id
                self.nodes2D[i][j + 1].edgeCost = currentNode.edgeCost+1
                self.nodes2D[i][j + 1].heuristicFn=self.nodes2D[i][j + 1].edgeCost+self.nodes2D[i][j + 1].hOfN
                if self.nodes2D[i][j + 1] not in not_visited:
                    not_visited.append(self.nodes2D[i][j + 1])

        # fill path
        temp = endNode
        while temp.id != startNode.id:
            self.path.append(temp.id)
            for i in range(self.count_row):
                for j in range(self.count_nodes):
                    if self.nodes2D[i][j].id == temp.previousNode:
                        temp = self.nodes2D[i][j]
                        break
        self.path.append(startNode.id)
        self.path.reverse()

        # fill full path
        for item in visited:
            self.fullPath.append(item.id)

        self.totalCost = endNode.heuristicFn

        return self.path, self.fullPath, self.totalCost


def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
               #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

            #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
