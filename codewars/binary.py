def count_bits(n: int) -> int:
    """ Counts the number of 1 bits (set bits) in the binary representation of n """
    return f"{n:b}".count("1")