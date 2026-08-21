import urllib.request
import urllib.parse
import json

url = "https://itunes.apple.com/search?term=Annmary+Saji+Jasmine&entity=album"
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print("Apple Music:", data)
except Exception as e:
    print("Apple Music error:", e)

