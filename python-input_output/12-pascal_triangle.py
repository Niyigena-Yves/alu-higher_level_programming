#!/usr/bin/python3
"""Definition of a function."""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        tempo = [1]
        for a in range(len(t) - 1):
            tempo.append(t[a] + t[a + 1])
        tempo.append(1)
        tr.append(tempo)
    return tr
