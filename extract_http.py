import re
with open(r"C:\Users\dipuj\.gemini\antigravity\brain\c14d06b1-de1e-459e-b0a0-b5c562fb0328\.user_uploaded\media_1787330729847.pdf", 'rb') as f:
    content = f.read()
    
# Extract anything looking like http
urls = re.findall(b'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
for u in set(urls):
    print(u.decode('ascii', errors='ignore'))
