import urllib.request
import urllib.parse

url = "https://www.youtube.com/oembed?url=https://youtu.be/uyy00VsBLS4&format=json"
req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        print("Success:", response.read().decode()[:100])
except Exception as e:
    print("Error:", e)
