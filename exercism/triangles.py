def equilateral(sides):
    a, b, c = sides
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return True
        return False
    return False

def isosceles(sides):
    a, b, c = sides
    if a + b > c and b + c > a and a + c > b:
        if (a == b and b != c) or (c == b and c != a) or (a == c and a != b):
            return True
        return False
    return False

def scalene(sides):
    a, b, c = sides
    if a + b > c and b + c > a and a + c > b:
        if a != b and b != c and a != c:
            return True
        return False
    return False