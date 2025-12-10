def hakimi_havel(seq):
    seq = sorted(seq, reverse=True)
    d = seq[0]
    rest = seq[1:]

    if d > len(rest):
        return None

    for i in range(d):
        rest[i] -= 1
        if rest[i] < 0:
            return None

    return rest


def is_graph(seq):
    while any(x > 0 for x in seq):
        seq = hakimi_havel(seq)
        if seq is None:
            return False
    return True


print(is_graph([3,3,2,2,2]))