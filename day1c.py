__author__ = 'ortus'


def sumofsquares(m):
    i = 1
    sums = 0
    while i <= m:
        sums += i**2
        i += 1
    print(i)
    print(sums)

sumofsquares(5)