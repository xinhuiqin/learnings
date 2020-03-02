#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author  : Sweeneys
# @file   : dijkstra_algorithm.py
# @time   : 2020-02-19 09:44:17
# graph

# 存储每个节点的邻居和前往该邻居的开销
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# 存储每个节点的开销（节点的开销指的是从起点到该节点的“时间”）
infinity = float('inf')  # 未知的开销设为无穷大
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 存储父节点
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 标记已经处理过的节点
processed = []


def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node


node = find_lowest_cost_node(costs)  # 开销最小的节点
while node is not None:
	cost = costs[node]  # 获取该节点的开销
	neighbors = graph[node]  # 获取该节点的邻居
	for n in neighbors.keys():  # 遍历当前节点的所有邻居
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:  # 如果当前节点前往该邻居更近，
			costs[n] = new_cost  # 就更新该邻居的开销
			parents[n] = node  # 同时将该邻居的父节点设置为当前节点
	processed.append(node)  # 将当前节点标记为已处理
	node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环

print(costs)
print(parents)