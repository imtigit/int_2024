import requests
#output = requests.get('http://api.github.com')
output = requests.get('https://catfact.ninja/fact')
print(output)
print(output.url)
print(output.json)