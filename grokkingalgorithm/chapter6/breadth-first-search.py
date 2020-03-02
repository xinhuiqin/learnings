#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author  : Sweeneys
# @file   : breadth-first-search.py
# @time   : 2020-02-17 18:53:52
from collections import deque

# directed graph>hash table>dict
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['jonny', 'thom']
graph['peggy'] = []
graph['anuj'] = []
graph['jonny'] = []
graph['thom'] = []


# whether a person is a mongo seller
def person_is_seller(person):
	return person[-1] == 'm'


def search(name):
	# deque
	search_que = deque()
	search_que += graph[name]
	searched = []
	while search_que:
		person = search_que.popleft()
		if person not in searched:
			if person_is_seller(person):
				print(person + ' is a mongo seller')
				return True
			else:
				search_que += graph[person]
				searched.append(person)
	return False


# search('you')
my_deque = deque()
my_deque += graph['you']
print(my_deque)
# my_deque.append(graph['you'])
my_deque += graph['you']
print(my_deque)