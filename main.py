import requests

url  = 'https://softwareacademy.bg/index.php?q=group_in&id=448'

r = requests.get(url)
if r.ok:
    print(r.text)