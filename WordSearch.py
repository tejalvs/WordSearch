import sys
from collections import defaultdict

word_dictionary_final = []


def wordTraversal(graph, begin, end):
    visitedNodes = set()
    queue = [[begin]]
    while len(queue) >= 1:
        route = queue.pop(0)
        vertex = route[-1]
        if end == vertex:
            return route
        elif (vertex in visitedNodes)==False:
            for neighbour in graph.get(vertex, []):
                temporaryPath = list(route)
                temporaryPath.append(neighbour)
                queue.append(temporaryPath)
            visitedNodes.add(vertex)
    return None


def findLink(startWord, endWord):
    global word_dictionary_final
    graph = defaultdict(set)
    pathLength = 0
    if startWord == endWord:
        print("Error:enter two different words")
        return
    elif len(startWord) == 0 or len(endWord) == 0:
        print("Error:Enter both the words")
        return
    elif (startWord not in word_dictionary_final or endWord not in word_dictionary_final):
        print("Error:Words not available in dictionary")
        return
    elif (len(startWord) - len(endWord) != 0):
        print("Error:Enter both words of same length")
        return
    length = len(startWord)
    wordlink = defaultdict(list)
    graph = {}
    for word in word_dictionary_final:
        if len(word) == length:
            for i in range(length):
                groupName = word[:i] + "__addedTo__" + word[i + 1:]
                if (groupName in wordlink.keys()) == False:
                    wordlink[groupName] = [word]
                else:
                    wordlink[groupName].append(word)
    for groupName in wordlink.keys():
        for source in wordlink[groupName]:
            for destination in wordlink[groupName]:
                if source != destination:
                    if destination in graph.keys():
                        graph[destination].append(source)
                    else:
                        graph[destination] = [source]
                    if source in graph.keys():
                        graph[source].append(destination)
                    else:
                        graph[destination].append(source)
    finalPath = wordTraversal(graph, startWord, endWord)
    for i in range(0, len(finalPath)):
        if i < (len(finalPath) - 1):
            print(finalPath[i] + " --> ", end="")
        else:
            print(finalPath[i])
    print("steps :", len(finalPath) - 1)


def getdictionary():
    global word_dictionary_final, alphabet_list
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    words = open("/usr/share/dict/words", 'r')
    word_dictionary = words.readlines()
    for word in word_dictionary:
        word = word.translate({ord('\n'): None})
        word_dictionary_final.append(word)


getdictionary()
findLink(sys.argv[1], sys.argv[2])
