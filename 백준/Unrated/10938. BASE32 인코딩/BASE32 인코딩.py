import base64
print(base64.b32encode(input().encode("ascii")).decode("ascii"))