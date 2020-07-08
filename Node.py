from collections import defaultdict
from itertools import product
import os
from collections import deque

def build_graph(words):
    buckets = defaultdict(list)
    graph = defaultdict(set)

    for word in words:
        for i in range(len(word)):
            bucket = '{}_{}'.format(word[:i], word[i + 1:])
            buckets[bucket].append(word)

    # add vertices and edges for words in the same bucket
    for bucket, mutual_neighbors in buckets.items():
        for word1, word2 in product(mutual_neighbors, repeat=2):
            if word1 != word2:
                graph[word1].add(word2)
                graph[word2].add(word1)

    return graph


def get_words(vocabulary_file):
    for line in open(vocabulary_file, 'r'):
        yield line[:-1]  # remove newline character


vocabulary_file = os.path.join(os.path.dirname(__file__), 'exampleWords.txt')
word_graph = build_graph(get_words(vocabulary_file))





def traverse(graph, starting_vertex):
    visited = set()
    queue = deque([[starting_vertex]])
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        yield vertex, path
        for neighbor in graph[vertex] - visited:
            visited.add(neighbor)
            queue.append(path + [neighbor])

if __name__ == '__main__':
    for vertex, path in traverse(word_graph, 'ABASE'):
        if vertex == 'ABASH':
            print(" -> ".join(path))
            # FOOL -> FOOD -> FOLD -> SOLD -> SOLE -> SALE -> SAGE

# word_graph['FOOL']
# set(['POOL', 'WOOL', 'FOWL', 'FOAL', 'FOUL', ... ])