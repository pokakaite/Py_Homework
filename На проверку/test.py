from hashlib import md5, sha1, sha256
from uuid import uuid4

s = md5(b'lol')
print(dir(s))
print(s.hexdigest()) # 9cdfb439c7876e703e307864c9167a15

print(uuid4())