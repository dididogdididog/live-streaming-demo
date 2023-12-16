import requests

ip='192.168.1.109'
url = f'http://{ip}:4000/api'
data={"text":"Hello, nice to meet you. Welcome to acl lab."}
response = requests.post(url,json=data)

# Print the response status code and content
print('Status Code:', response.status_code)
print('Response Content:', response.text)
