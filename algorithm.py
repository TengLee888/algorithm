

# Binery Search
def binery_search(list , item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) //2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

myList = [1,3,5,7,9]

print (binery_search(myList , 3))
print (binery_search(myList , -1))


# Sort
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1 , len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
        并且返回该元素的值。
    return newArr

print (selectionSort([5,3,6,2,10]))



# Recursive
def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print (sum([5,3,6,2,10]))


#pg4-9 4.2
def listCount(list):
    if list == []:
        return 0
    return 1 + listCount(list[1:])

print (listCount([5,3,6,2,10]))



#pg4-9 4.3
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print (max([5,3,6,2,10]))


#quicksort
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

quicksortList = [2,4,6,3,5,8,4,2,6,8,3,5,6,3,6,7]

print (quicksort(quicksortList))


# Queue
from collections import deque

# 要先建立Hach map
# graph = {}
# graph['you'] = ['alice','bob','claire']
# graph['alice']=['peggy']
# graph['bob']=['anuj','peggy']
# graph['claire']=['thom','jonny']
# graph['anuj']=[]
# graph['peggy']=[]
# graph['thom']=[]
# graph['jonny']=[]


def search(name):
    searchQueue = deque()
    searchQueue += graph[name]
    searched = []
    while searchQueue:
        checkname = searchQueue.popleft()
        if checkname not in searched:
            if personIsSeller(checkname):
                print(checkname + ' is a seller!')
                return True
            else:
                searched.append(checkname)
                searchQueue += graph[checkname]
    return False

def personIsSeller(name):
    return name[-1] == 'm'

search('you')


# Dijkstra's algorithm

#圖形雜湊表
graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b']= 2
graph['a'] = {}
graph['a']['c'] = 4
graph['a']['d'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['d'] = 7
graph['c'] = {}
graph['c']['d'] = 6
graph['c']['fin'] = 3
graph['d'] = {}
graph['d']['fin'] = 1
graph['fin'] = {}

#成本雜湊表
infinity = float("inf")
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['fin'] = infinity


#父項雜湊表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

proceeded = []

def findLowestCost(costs):
    # print ('costs: ')
    # print (costs)
    lowestCost = float("inf")
    # print ('lowestCost: ')
    # print (lowestCost)
    lowestCostNode = None
    for node in costs:
        # print ('node: ')
        # print (node)
        cost = costs[node]
        if cost < lowestCost and node not in proceeded:
            # lowestCost = cost
            lowestCostNode = node
            print ('lowestCostNode,lowestCost')
            print (lowestCostNode,lowestCost)
    return lowestCostNode


node = findLowestCost(costs)
# print ('return: ' + node)
while node is not None:
    # print ('node: ')
    # print (node)
    cost = costs[node]
    neighbors = graph[node]
    # print (neighbors)
    for n in neighbors.keys():
        # print ('n: ' + n)
        # print (neighbors[n])
        newCost = cost + neighbors[n]
        #下面會出錯，因為目前還不知道costs[d]
        if costs[n] > newCost:
            costs[n] = newCost
            parents[n] = node
    proceeded.append(node)
    print(proceeded)
    node = findLowestCost(costs)


#station question
stationNeeded = set(['mt','wa','or','id','nv','ut','ca','az'])

stations = {}
stations['kone']=set(['id','nv','ut'])
stations['ktwo']=set(['wa','id','mt'])
stations['kthree']=set(['or','nv','ca'])
stations['kfour']=set(['nv','ut'])
stations['kfive']=set(['ca','az'])

finalStation = set()


while stationNeeded:
    bestStation = None
    stateCovered = set()
    for station, stateStation in stations.items():
        covered = stationNeeded & stateStation
        #print (station , len(covered) , len(stateCovered))
        if len(covered) > len(stateCovered):
            bestStation = station
            stateCovered = covered
        print('bestStation: 'bestStation)
    stationNeeded -= stateCovered
    finalStation.add(bestStation) 
    print('finalStation: ' , finalStation)
print(finalStation)
