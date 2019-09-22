import re

teststr = "hello 1231, hello world. hello chowming"


splittest = re.split(r"[\.,\s]+", teststr)
print(splittest)


if re.match(r".*", teststr):
    print("matched")
else:
    print("not matched")

teststr = "028-5771819"

m = re.match(r"(\d{3})-(\d{7})", teststr)
print(m)

print(m.group(0))

print(m.group(1))

print(m.group(2))


print(m.groups())

for i in m.groups():
    print(i)


from datetime import datetime

now = datetime.now()

print(now)

print(type(now))

dt = datetime(2019,1,1,0,0,0)

print(type(dt))

print(now.timestamp())

print(dt.timestamp())

ts = 0

print(datetime.fromtimestamp(ts))

print(datetime.utcfromtimestamp(ts))


import base64
print(base64.b64encode(b"hello worod"))



import hashlib

f = open("test", "r")
md5 = hashlib.md5()
md5.update(f.read().encode("utf-8"))
print(md5.hexdigest())

f.close()