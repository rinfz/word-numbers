from functools import reduce
from itertools import chain, tee

def foldr(fn, acc, xs):
    yield reduce(lambda x, y: fn(y, x), reversed(list(xs)), acc)

def add(left, right):
    yield from chain(left, right)

def mul(left, right):
    cached = []
    for x in left:
        for y in right:
            cached.append(y)
            yield x + y
        break
    for x in left:
        for y in cached:
            yield x + y

def muli(l, r):
    yield from mul(iter(l), iter(r))

def zero():
    return []

def one():
    return [""]

def snr(*values):
    yield from values

def product(xs):
    yield from foldr(mul, one(), xs)

def string(s):
    yield from product(s)

def sum_(xs):
    yield from foldr(add, zero(), xs)

def strings(s):
    yield from sum_(string(p) for p in s.split())

def prefixes():
    return snr("fif", "six", "seven", "eigh", "nine")

ten1_a, ten1_b, ten1_c = tee(
    snr("one", "two", "three", "four", "five", "six", "seven", "eight", "nine"),
    3
)

ten2_a, ten2_b = tee(reduce(
    add,
    [
        ten1_a,
        snr("ten", "eleven", "twelve"),
        mul(add(snr("thir", "four"), prefixes()), snr("teen")),
        mul(
            mul(add(snr("twen", "thir", "for"), prefixes()), snr("ty")),
            add(one(), ten1_b),
        ),
    ],
))

ten3_a, ten3_b, ten3_c, ten3_d = tee(add(
    ten2_a,
    mul(mul(ten1_c, snr("hundred")), add(one(), ten2_b)),
), 4)

ten6_a, ten6_b = tee(add(
    ten3_a,
    mul(mul(ten3_b, snr("thousand")), add(one(), ten3_c)),
))

ten9 = add(
    ten6_a,
    mul(mul(ten3_d, snr("million")), add(one(), ten6_b)),
)

def last(it):
    for x in it: pass
    return x

print(last(ten6_a))
print(len(''.join(ten6_b)))
