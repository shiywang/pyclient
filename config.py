
request_headers = {'Content-Type': 'application/json', 'Authorization': 'Token d1f345f5d081d6ee3e64f4d4f2883866233d4ff4'}
test_device_id      = "F43053011ACF"
test_device_type    = "RRI"
filename = "./data_store/test.txt"


#base_ip = "127.0.0.1"
base_ip = "172.24.41.203"
base_port = "8000"
base_url = "http://" + base_ip + ":" + base_port + "/"
ws_url = "ws://" + base_ip + ":" + base_port + "/ws/sensor/RR"