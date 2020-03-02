#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @author  : Sweeneys
# @file   : chapter8.py
# @time   : 2020-02-20 07:38:27

# 创建一个集合，包含所有未覆盖的州
states_needed = set(
	['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']
)

# 广播台清单
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 最终选择的广播台
final_station = set()

while states_needed:
	# 最佳的广播台——覆盖了最多的未覆盖的州
	best_station = None

	# 最佳广播台覆盖的所有未覆盖的州
	state_covered = set()

	for station, states_for_station in stations.items():
		covered = states_needed & states_for_station  # 交集
		if len(covered) > len(state_covered):
			best_station = station
			state_covered = covered

	final_station.add(best_station)
	states_needed -= state_covered  # 剩下的未覆盖的州
print(final_station)