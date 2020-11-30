from typing import List, Tuple
import random


def make_pairs(A: List[int], n: int) -> List[Tuple[int, int]]:
    """
    A brute-force implementation that was kept for comparison
    """
    res = []
    if not A:
        return res
    for x1 in range(len(A)):
        for x2 in range(len(A)):
            if x1 != x2 and A[x1] + A[x2] == n:
                res.append((A[x1], A[x2]))
    return res


def make_pairs_faster(A: List[int], n: int) -> List[Tuple[int, int]]:
    """
    This function returns a list of pairs that sums equal to n.
    The pairs that are formed as (A[x1],A[x2])) and (A[x2],A[x1]))
    even if A[x1]==A[x2] are considered different but pairs that
    are formed by the same list item, ex: (A[x1],A[x1])), are excluded
    Args:
        :param A: a list of numbers
        :param n: a sum of two numbers
    Returns:
        A list of complementary pairs
    """
    res: List[Tuple[int, int]] = list()
    counters: Dict[int, int] = dict()

    if not A:
        return res

    for a in A:
        if a in counters:
            counters[a] += 1
        elif a == n/2:
            counters[a] = 0
        else:
            counters[a] = 1

    for a in A:
        if n - a in counters:
            pair = (a, n - a)
            for _ in range(counters[n-a]):
                res.append(pair)
    return res


def make_pairs_pythonic(A: List[int], n: int) -> List[Tuple[int, int]]:
    """
    The same function as above but written in idiomatic way
    Args:
        :param A: a list of numbers
        :param n: a sum of two numbers
    Returns:
        A list of complementary pairs
    """
    res: List[Tuple[int, int]] = list()
    counters: Dict[int, int] = dict()

    if not A:
        return res

    for a in A:
        counters[a] = counters.get(a, -1 if a == n/2 else 0) + 1

    res = [pair for a in A if n-a in counters for pair in [(a, n-a)] * counters[n-a]]

    return res

# k = 3
# a = [2, 2, -3, 0, 1, 3, -2, 4, 5, -6]

k = random.randint(0, 10)
a = []
for i in range(10):
    sign = (-1)**random.randint(0, 5)
    a.append(int(random.random()*sign*10))

print("k = {}\n"
      "a = {}\n" \
      "{}\n" \
      "{}\n" \
      "{}".format(k, a, make_pairs(a, k), make_pairs_faster(a, k), make_pairs_pythonic(a, k)))
