#!/usr/bin/env python


from TCP import *
import argparse
import yaml
import time
import math


def main():

	# Parsing user input
	parser = argparse.ArgumentParser()
	parser.add_argument(
			'-p','--port',
			nargs='?',
			type=int,
			default=8118,
			help='TCP Port Number.'
		)
	parser.add_argument(
			'-i','--ip',
			nargs='?',
			type=str,
			default='127.0.0.1',
			help='TCP IP Address.'
		)
	parser.add_argument(
			'-b','--buffer_size',
			nargs='?',
			type=int,
			default=256,
			help='TCP Socket Buffer Size.'
		)
	parser.add_argument(
			'-m','--mode',
			nargs='?',
			action='store',
			default='client',
			choices=['client','server'],
			help='Client or Server mode.'
		)
	args = parser.parse_args()

	tcp = TCP(
		port		= args.port,
		ip			= args.ip,
		buffer_size	= args.buffer_size,
		mode		= args.mode,
	)


	# Keeps requesting the most recent data
	if(tcp.mode=='client'):
		try:
			for i in range(15):
				print i, yaml.load(tcp.request('kayak_0'))
				time.sleep(0.5)
		except:
			pass


	# Keeps providing the most recent data
	sim_update_secs = 0.010
	rotation_freque = 0.010
	if(tcp.mode=='server'):
		t = 0.000
		try:
			while True:
				tcp.database = {
					'kayak_0': yaml.dump({
							'Depth': 0.0,
							'Latitude': 32.0 	+ math.sin(rotation_freque*2*math.pi*t),
							'Longitude': -119.0	+ math.cos(rotation_freque*2*math.pi*t),
							'Salinity': 33.0	+ math.sin(0.25*2*math.pi*t),
							'Temperature': 16.0	+ math.sin(0.50*2*math.pi*t),
							'w': 1.0,
							'x': 0.0,
							'y': 0.0,
							'z': 0.0,
						}),
					'kayak_1': yaml.dump({
							'Depth': 0.0,
							'Latitude': 32.0 	+ math.cos(rotation_freque*2*math.pi*t),
							'Longitude': -119.0	+ math.sin(rotation_freque*2*math.pi*t),
							'Salinity': 33.0	+ math.sin(0.25*2*math.pi*t),
							'Temperature': 16.0	+ math.sin(0.50*2*math.pi*t),
							'w': 1.0,
							'x': 0.0,
							'y': 0.0,
							'z': 0.0,
						}),
					'glider_0': yaml.dump({
							'Depth': 50.0,
							'Latitude': 32.0 	+ math.sin(rotation_freque*2*math.pi*t),
							'Longitude': -119.0	+ math.cos(rotation_freque*2*math.pi*t),
							'Salinity': 33.0	+ math.sin(0.25*2*math.pi*t),
							'Temperature': 16.0	+ math.sin(0.50*2*math.pi*t),
							'w': 1.0,
							'x': 0.0,
							'y': 0.0,
							'z': 0.0,
						}),
					'glider_1': yaml.dump({
							'Depth': 100.0,
							'Latitude': 32.0 	+ math.cos(rotation_freque*2*math.pi*t),
							'Longitude': -119.0	+ math.sin(rotation_freque*2*math.pi*t),
							'Salinity': 33.0	+ math.sin(0.25*2*math.pi*t),
							'Temperature': 16.0	+ math.sin(0.50*2*math.pi*t),
							'w': 1.0,
							'x': 0.0,
							'y': 0.0,
							'z': 0.0,
						}),
				}
				t += sim_update_secs
				time.sleep(sim_update_secs)
				
		except:
			tcp.exit_server()



if __name__ == "__main__":
	main()
