#!/usr/bin/env python3
import json
import requests
# include standard modules
import argparse

class Restful:
	url = 'https://jsonplaceholder.typicode.com'

	def run(self, args):
		if args.METHOD == 'get':		
			Restful.get(args.ENDPOINT)
		if args.output and args.METHOD == 'get':		
			Restful.getOutput(args.ENDPOINT, args.output)
		if args.METHOD == 'post':
			Restful.post(args.ENDPOINT, args.data)
		if args.output and args.METHOD == 'post':		
			Restful.postOutput(args.ENDPOINT, args.data, args.output)

	def get(self, endpoint):
		response = requests.get(self.url + endpoint)
		self.handleError(response.status_code)		
		print(response.text)

	def getOutput(self, endpoint, file):
		response = requests.get(self.url + endpoint)
		self.handleError(response.status_code)	
		self.output(file,response.text)

	def post(self, endpoint, data):
		response = requests.post(self.url + endpoint, data)
		self.handleError(response.status_code)	
		print(response.text)

	def postOutput(self, endpoint, data, file):
		response = requests.post(self.url + endpoint, data)	
		self.handleError(response.status_code) 
		self.output(file,response.text)

	def output(self, file, data):
		with open(file, 'w') as outfile:
			json.dump(data, outfile)

	def handleError(self, status_code):
		if status_code >= 200 and status_code <= 299:
			print(status_code)
		else:
			print(str(status_code) + '- FAILURE')		
		


if __name__ == '__main__':
	# initiate the parser
	parser = argparse.ArgumentParser()
	parser.add_argument('METHOD', metavar='{get, post}', help='Request method')
	parser.add_argument('ENDPOINT', metavar='endpoint', help='Request endpoint URI fragment')
	parser.add_argument('-d', '--data', help="Data to send with request")
	parser.add_argument("-o", "--output", help="Output to .json or .csv file (default: dump to stdout)")
	                       
	# read arguments from the command line
	args = parser.parse_args()
	Restful = Restful()
	Restful.run(args)

