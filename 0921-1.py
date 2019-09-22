
import pickle
import json
l = ["hello world", "my name is chowming", 1, 2]

out = pickle.dumps(l)
print(out)

with open("list", "wb") as f:
    pickle.dump(l,f)


f = open("list", "rb")

d = pickle.load(f)

f.close()
print(d)

out = json.dumps(l)

print(out)


f = open("json", "w")
f.write(out)
f.close()

f = open("json", "r")
out = f.read()
dic = json.loads(out)
print(dic)