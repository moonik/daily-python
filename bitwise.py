def reverse(v):
    print("{0:b}".format(v))
    r = v
    s = 31
    v >>= 1
    while v > 0:
        r <<= 1
        r |= v & 1
        s -= 1
        v >>= 1
    r <<= s
    print("{0:b}".format(r))


def find_lowest_not_set(x):
    return ~x & (x + 1)


reverse(5)

