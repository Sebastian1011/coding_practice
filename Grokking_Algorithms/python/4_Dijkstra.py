#!/usr/bin/env python
#-*- coding: utf-8 -*-

#   graph:
#   start   -6->    A
#   start   -2->    b
#   A       -1->    dest
#   B       -3->    A
#   B       -5->    dest
#

def find_lowest_cost_node(costs):
    pass

def dijkstra():
    graph = {}
    graph['start'] ={}
    graph['start']['A'] = 6
    graph['start']['B'] = 2
    graph['A'] = {}
    graph['A']['dest'] = 1
    graph['B'] = {}
    graph['B']['A'] = 3
    graph['B']['dest'] = 5
    infinity = float('inf')
    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['dest'] = infinity
    parents = {}
    parents['A'] = 'start'
    parents['B'] = 'start'
    parents['dest'] = None
    processed = []
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(graph)


if __name__=='__main__':
    dijkstra()