import re
with open(r"C:\Users\dipuj\.gemini\antigravity\brain\c14d06b1-de1e-459e-b0a0-b5c562fb0328\.user_uploaded\media_1787330729847.pdf", 'rb') as f:
    content = f.read()
    
# Extract anything looking like a URL
urls = re.findall(b'URI\s*\(([^)]+)\)', content)
for u in urls:
    print(u.decode('ascii', errors='ignore'))
