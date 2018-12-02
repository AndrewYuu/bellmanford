#Andrew Yu 110340834
#Bryan Valarezo 110362410

fileName = input("What is the name of the file?: \n")
inputFile = open(fileName, "r", encoding='utf-8')

graph = [] #for our graph edges and nodes --> src, dest, weight
nodeDict = {} #for storing node mappings
nodePathDict = {} #for storing predecessors
allNodes = set() #for all nodes read in from file.
numberOfNodes = 0
index = 0 #for node mappings

#initialize graph and all other overhead
for line in inputFile:
    currentLine = line.split(",")
    node1 = currentLine[0]
    node2 = currentLine[1]
    weight = currentLine[2]
    graph.append([node1, node2, weight])
    allNodes.add(node1)
    allNodes.add(node2)
    if node1 not in nodeDict:
        nodeDict[node1] = index
        index = index + 1
        nodePathDict[node1] = None
    if node2 not in nodeDict:
        nodeDict[node2] = index
        index = index + 1
        nodePathDict[node2] = None


numberOfNodes = len(allNodes)
sourceNode = "x"
distances = [float("Inf")] * numberOfNodes #init all distances at every node to infinity.
distances[nodeDict[sourceNode]] = 0 #distance of the source node is 0

#get the path by reverse search from y to x (predecessors)
def getPath(nodePathDict, src, dest):
    if(nodePathDict.get(src) == dest):
        print(dest, end=" ")
        print(src, end=" ")
    else:
        getPath(nodePathDict, nodePathDict.get(src), dest)
        print(src, end=" ")

#bellman ford
for i in range(numberOfNodes - 1):
    for node1, node2, weight in graph:
        if distances[nodeDict[node1]] != float("Inf"):
            if distances[nodeDict[node1]] + int(weight) < distances[nodeDict[node2]]:
                distances[nodeDict[node2]] = distances[nodeDict[node1]] + int(weight)
                nodePathDict[node2] = node1


#print distance to source y
for node in allNodes:
    if(node == 'y'):
        print('The distance is: %d' % (distances[nodeDict[node]]))

#print path
print('The shortest path is: ', end=" ")
getPath(nodePathDict, 'y', 'x')