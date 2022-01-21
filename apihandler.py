import requests
import queue
import threading
import json

api_user = "test1"
api_password = "test"
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
api_url =  "http://" + base_url + ":" + port + "/"
=======
=======
api_url =  "http://" + base_url + ":" + port + "/"
=======
>>>>>>> fix import url circle

request_headers = {'Content-Type': 'application/json'}
api_url = ''

class ApiHandler(threading.Thread):
	def __init__(self, url):
		super(ApiHandler, self).__init__()
		self.__output_queue = queue.Queue()
		self.__function_queue = queue.Queue()
		self.timeout = 1.0/60
		self.api_url = url

	def onThread(self, function, *args, **kwargs):
		self.__function_queue.put((function, args, kwargs))

	def create_senior(self, data):
		r = requests.post(self.api_url+"seniors/", headers=request_headers, auth=(api_user, api_password), data=data)
		if r.status_code == 201:
			return True
		else:
			print(r.json())
			return False

	def delete_user(self, device_id):
		r = requests.delete(self.api_url+"seniors/"+device_id, auth=(api_user, api_password))

	def send_data(self, senior):
		device_type = senior.device.type.name
		data = senior.get_data()
		url = self.api_url + "sensordata/" + device_type + '/'
		r = requests.post(url, headers=request_headers, auth=(api_user, api_password), data=json.dumps(data))

	def send_ping(self, senior):
		data = {
			"device_id": senior.id,
			"battery": senior.get_battery(),
		}
		url = self.api_url + "ping/"
		r = requests.post(url, headers=request_headers, auth=(api_user, api_password), data=json.dumps(data))

	def run(self):
		print("Starting API Handler")
		while True:
			try:
				# Get functions called on this thread
				function, args, kwargs = self.__function_queue.get(timeout=self.timeout)
				function(*args, **kwargs)			
			except Exception as e:
				pass
>>>>>>> format update and parameterized url endpoint

>>>>>>> fix import url circle
request_headers = {'Content-Type': 'application/json'}
=======
request_headers = {'Content-Type': 'application/json', 'Authorization': 'Token 79bfff7c4e78a575af2226fde003609680112e85'}
>>>>>>> remove apihander class
api_url = ''

=======
request_headers = {'Content-Type': 'application/json', 'Authorization': 'Token 79bfff7c4e78a575af2226fde003609680112e85'}
api_url = ''

>>>>>>> remove apihander class
# to be called from another thread on program exit
<<<<<<< HEAD
<<<<<<< HEAD
def custom_senior_delete(device_id, url):
	r = requests.delete(url+"seniors/"+device_id, auth=(api_user, api_password))


def custom_create_senior(data, url):
	r = requests.post(url+"seniors/", headers=request_headers, data=data)
=======
def custom_senior_delete(device_id):
	r = requests.delete(api_url+"seniors/"+device_id, auth=(api_user, api_password))


def custom_create_senior(data):
	r = requests.post(api_url+"seniors/", headers=request_headers, auth=(api_user, api_password), data=data)
>>>>>>> format update and parameterized url endpoint
=======
def custom_senior_delete(device_id, url):
	r = requests.delete(url+"seniors/"+device_id, auth=(api_user, api_password))


def custom_create_senior(data, url):
<<<<<<< HEAD
	r = requests.post(url+"seniors/", headers=request_headers, auth=(api_user, api_password), data=data)
>>>>>>> fix import url circle
=======
	r = requests.post(url+"seniors/", headers=request_headers, data=data)
>>>>>>> remove apihander class
	if r.status_code == 201:
		print(r.json())
		return True
	else:
		print(r.json())
		return False


