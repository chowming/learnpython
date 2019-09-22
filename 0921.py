from io import StringIO

file = open("note.txt", "r")

print(file)
print(file.read())


# with open("note.txt", "r") as f:
#     print(f.readlines())

# lines = f.readline()
f = open("note.txt", "r")
for line in f.readlines():
    print(line)

f.close()

f = open("note1.txt", "w")
f.write("hello wrold")
f.close()

f = open("test.jpg", "rb")
content = f.read()


with open("note1.txt", "w") as f:
    f.truncate(0)
    for i in range(10):
        f.write("hello world\n")

with open("note1.txt", "a") as f:
    # f.truncate(0)
    for i in range(10):
        f.write("hello world\n")




f = StringIO()
for i in range(10):
    f.write("hello world\n")

print(f.getvalue())

f.truncate(0)
print(f.getvalue())


import os
print(os.name)
print(os.environ)


print(os.curdir)

if ("testdir"):
    print("testdir is dir")
os.chdir("testdir")
for i in range(1000):
    with open("test %d.txt" % i, "w") as f:
        f.write("hello %d" % i)


os.chdir("..")

print(os.curdir)

