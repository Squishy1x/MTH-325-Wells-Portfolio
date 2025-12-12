# Hakimi-Havel step
def hakimi_havel(seq):
    # Sort the sequence in non-increasing order
    seq = sorted(seq, reverse=True)
    d = seq[0]
    rest = seq[1:]

    # A node cannot connect to more nodes than are available
    if d > len(rest):
        return None

    for i in range(d):
        rest[i] -= 1

        # If any degree is negative, the sequence is not graphic
        if rest[i] < 0:
            return None

    # Return the new sequence for the next iteration without the first element
    return rest


def is_graph(seq):
    # Continue as long as there are positive degrees
    while any(x > 0 for x in seq):
        # Apply reduction step
        seq = hakimi_havel(seq)

        # If returns None, a non-graphic condition was met
        if seq is None:
            return False
        
    return True


print(is_graph([3,3,2,2,2]))