import hashlib

HASH_NAME = "sha256" # hash algorithm (md5,sha1,sha224,sha256,sha384,sha512)
txt = input()
text = txt.encode('utf-8')
t = hashlib.new(HASH_NAME)
t.update(text)
result = t.hexdigest()
print(result)