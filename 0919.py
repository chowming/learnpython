from math import sqrt
#function test
intlist = [100,-100, 3.13, -123.123]

for i in intlist:
    print(abs(i))

print(max(intlist))


print(int('1231'))



def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


print(my_abs(-123))


def null_fun():
    pass

print(null_fun())

#null_fun(1)

def my_fun(x):
    if not isinstance(x, (float, int)):
        raise TypeError("bad operate type")
    if x > 0:
        return x
    else:
        return -x;


for i in intlist:
    print(my_fun(i))

#my_fun("0x123132")


def multi_ret(nx, ny):
    return nx,ny

print(multi_ret(1,2))

def quadratic(a, b, c):
    if a == 0:
        x1 = -b / c
        return x1
    x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2

print(quadratic(1, 2, 1))
print(quadratic(1, -2, 1))
print(quadratic(0, -2, 1))


def power(x, n):
    i = 0
    ret = 1;
    while i < n:
        i = i + 1
        ret = ret * x;
    return ret


print(power(100, 20))
print(power(100, -1))


def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


print(fact(100))

def default_arg(x,y=120):
    print(x * y)
    return

print(default_arg(1))
print(default_arg(100,9))

