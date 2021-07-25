#!/usr/bin/env python3

import json
import requests


def find_a_server_in(locations: list, tiers: list) -> list:
	response = requests.get('https://api.protonmail.ch/vpn/logicals')
	servers_dict = json.loads(response.text)
	
	locFilter = lambda x: (not locations) ^ bool(sum(loc in x for loc in locations))
	tierFilter = lambda x: (not tiers) ^ (x in tiers)
	filterFunc = lambda x: locFilter(x['Name']) & tierFilter(x['Tier'])

	workSpace = list(filter(filterFunc, iter(servers_dict['LogicalServers'])))
	if not workSpace: return []
	bestLoad = min(map(lambda x: x['Load'], iter(workSpace)))
	return list(filter(lambda x: x['Load'] == bestLoad, iter(workSpace)))

