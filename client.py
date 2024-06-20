import requests

ip='127.0.0.1'
url = f'http://{ip}:4000/api'
data={"text":"Hello, welcome to ACL lab."}
response = requests.post(url,json=data)

# Print the response status code and content
print('Status Code:', response.status_code)
print('Response Content:', response.text)
