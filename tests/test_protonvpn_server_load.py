#!/usr/bin/env python3

import argparse
import protonvpn_server_load as vpn


def input(args):
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', '--location', type=str, nargs='*', default=[], help='The Country Code of the VPN Location')
	parser.add_argument('-t', '--tiers', type=int, nargs='*', default=[], help='The tiers to filter on')

	return vars(parser.parse_args(args))

def test_protonvpn_server_load(capsys):
	inputDict = input(['-t', '0', '-l', 'US'])
	bestServers = vpn.find_a_server_in(inputDict['location'], inputDict['tiers'])
	with capsys.disabled():
		print(*map(lambda server: server['Name'] + ": " + str(server['Load']) + "%", bestServers),sep='\n')
	assert len(bestServers)

def test_version():
    assert vpn.__version__ == '0.1.0'

