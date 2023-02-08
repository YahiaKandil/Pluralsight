import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

for person in json['people']:
    print('\n'+ person['name'])

print("\n")
