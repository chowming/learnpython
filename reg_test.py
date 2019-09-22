import re

pat = r"\d{4,12}"
desstr = "123-13213132-312321"
m = re.search(pat, desstr)

print(m.group())

m = re.findall(pat, desstr);
if m:
    print(m)
else:
    print("not match %s" % desstr)

pat1 = r"(?P<num>\d{5})"

m = re.search(pat1, desstr)
print(m.group('num'))

str = "_"

res = re.search(r"[\_]", str)
print(res.group())

with open("dream.txt", "r") as f:
    teststr = f.read()


res = re.split(r"[\"\'\,\.\!\s]+", teststr)
print(res)
sortedres = sorted(res)
print(sortedres)

print(len(sortedres))
setres = set(sortedres)

print(len(setres))
print(setres)


emal_req = r"(^[\w][\w\.]*)@[\w][\w\.]*com"
test_emal = "bill.gates@microsoft.com"

res = re.search(emal_req, test_emal)
print(res.group())

test_emal = "someone@email.com"
res = re.search(emal_req, test_emal)
print(res.group())


emal_req = r"(?P<email_name>^[\w][\w\.]*)@[\w][\w\.]*com"
res = re.search(emal_req, test_emal)
print(res.group('email_name'))


test_emal = "bill.gates@microsoft.com"
res = re.search(emal_req, test_emal)
print(res.group('email_name'))

restr = r"dream"
repat = re.compile(restr)

reresult = repat.findall(teststr)
if reresult:
    print(reresult)
else:
    print("Can not mat")

reresult = repat.search(teststr)
print(reresult.span())

reresult = repat.finditer(teststr)

for i in reresult:
    print(i.span())


DREAM_RE = re.compile(r"DREAM.*dream", re.IGNORECASE | re.DOTALL)

reresult = DREAM_RE.finditer(teststr)
if reresult:
    for i in reresult:
        print(i.span())
        print(i.group())
else:
    print("not matched")

# ZHONGWENSTR = "我是周明，你睡睡"
#
# zhongwenre = r"\w+"
#
# zwrepat = re.compile(zhongwenre, re.LOCALE);
#
# zwres = re.search(ZHONGWENSTR.encode('utf-8'))
# if zwres:
#     print(zwres.group())
# else:
#     print("not match")


str = "i have a dream."

p = re.compile(r"\ba\b")

print(p.search(str).span())

p = re.compile(r"\Ba\B")
print(p.search(str).span())

p = re.compile(r"\Ba\b")
print(p.search("Data").span())



str = re.sub(r"dream", "Dream", teststr)
print(str)

with open("dream.txt", "w") as f:
    f.truncate(0)
    f.write(str)
    f.close()
