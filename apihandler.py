import requests
from config import request_headers


# to be called from another thread on program exit
def custom_senior_delete(device_id, url):
	r = requests.delete(url+"backend/api/seniors/"+device_id, headers=request_headers)


def custom_create_senior(data, url):
	print(url)
	r = requests.post(url+"backend/api/seniors/", headers=request_headers, data=data, verify='/etc/ssl/certs/ca-certificates.crt')
	if r.status_code == 201:
		# print(r.json())
		return True
	else:
		# print(r.json())
		return False


