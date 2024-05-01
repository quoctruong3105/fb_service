import requests

url = 'http://localhost:3105/add_new_page'
response = requests.post(url, json={'page_id': "12321312321", 'token': '312321321312'})

print(response.status_code)
print(response.json())
