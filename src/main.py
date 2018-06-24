#!/usr/bin/env python


from TCP import *
import argparse
import yaml

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
				print i, tcp.request('glider-01')
				print i, tcp.request('glider-02')
		except:
			pass


	# Keeps providing the most recent data
	if(tcp.mode=='server'):
		counter = 0
		try:
			while True:
				counter += 1
				tcp.database = {
					'glider-01': 'The glider-01 value is %d'%counter,
					'glider-02': 'The glider-02 value is %d'%counter,
				}
				
		except:
			tcp.exit_server()



if __name__ == "__main__":
	main()
