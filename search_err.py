import urllib.request
import json
req = urllib.request.Request("https://api.duckduckgo.com/?q=youtube+embed+error+153&format=json")
try:
    with urllib.request.urlopen(req) as response:
        print(response.read().decode()[:500])
except Exception as e:
    print(e)
