def Karatsuba(x: int, y: int) -> int:
    """
    Calculate the multiplication between two integers using Karatsuba's method
    Python uses a better method, just treat this as a showcase on how to  write this method
    :param x:
    :param y:
    :return:
    """
    # Since we have to multiply at some point, we do so when it is smaller than 10
    # It is possible to mathematically calculate when the Karatsuba method is better than the 'normal method', but as a
    # Human that uses base 10, this makes sense
    if x < 10 and y < 10:
        return x * y

    # While it is possible to use max / min / any of the two, using max enables to be more efficient by splitting the
    # Bigger number fewer times than if we had used the smallest number ( eg : Splitting 7,163,732 gives less
    # Sub-problems than if we split it using 1 as a base )
    n = max(len(str(x)), len(str(y)))

    # Floor the division of n by 2 ( n // 2 ) and in case n is odd, we round it up using n & 1 ( equal to n % 2 )
    nby2 = (n >> 1) + (n & 1)

    # Floor the division of x by 2^n ( x // 2**nby2 )
    a = x >> nby2
    # Put the remainder of said division into b, translated this gives b = x % 2**nby2
    b = x & ((1 << nby2) - 1)
    # Rince and repeat for y
    c = y >> nby2
    d = y & ((1 << nby2) - 1)

    # Calculate ac, bd and ( a + b )( c + d ), this is where we get rid of a multiplication
    ac = Karatsuba(a, c)
    bd = Karatsuba(b, d)
    e = Karatsuba(a + b, c + d) - ac - bd

    # Use more bit operators to return :
    # ac * 2**(2 * nby2) + e * 2**nby2 + bd
    return (ac << (nby2 << 1)) + (e << nby2) + bd
