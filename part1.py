from itertools import chain
from functools import reduce

def foldr(fn, acc, xs):
    # https://burgaud.com/foldl-foldr-python/
    return reduce(lambda x, y: fn(y, x), xs[::-1], acc)

class S:
    def __init__(self, values):
        self.values = values

    @classmethod
    def zero(cls):
        return cls([])

    @classmethod
    def one(cls):
        return cls([""])

    def __add__(self, other):
        return S(self.values + other.values)

    def __mul__(self, other):
        return S(
            list(chain.from_iterable(
                [[xs + ys for ys in other.values] for xs in self.values]
            ))
        )

    def __str__(self):
        return f"<{', '.join(self.values)}>"

    def __eq__(self, other):
        return self.values == other.values

    @classmethod
    def product(cls, xs):
        return foldr(cls.__mul__, cls.one(), xs)

    @classmethod
    def string(cls, s):
        return cls.product([cls([c]) for c in s])

    @classmethod
    def sum(cls, xs):
        return foldr(cls.__add__, cls.zero(), xs)

def strings(s):
    return S.sum([S.string(part) for part in s.split(' ')])

case1_a = (S(["twenty"]) + S(["thirty"])) * S(["", "one", "two"])
case1_b = S(["twenty"]) * S(["", "one", "two"]) + S(["thirty"]) * S(["", "one", "two"])
assert case1_a == case1_b, f"Case 1 failed:\n{case1_a}\n{case1_b}"

prefixes = strings("fif six seven eigh nine")
ten1 = strings("one two three four five six seven eight nine")
ten2 = ten1 \
     + strings("ten eleven twelve") \
     + (strings("thir four") + prefixes) * S.string("teen") \
     + (strings("twen thir for") + prefixes) * S.string("ty") * (S.one() + ten1)
ten3 = ten2 + ten1 * S.string("hundred") * (S.one() + ten2)
ten6 = ten3 + ten3 * S.string("thousand") * (S.one() + ten3)
# ten9 = ten6 + ten3 * S.string("million") * (S.one() + ten6)

print(len(''.join(ten6.values)))
print("done")
