def is_armstrong_number(number):
    digits = str(number)
    n = len(digits)
    total = 0
    for d in digits:
        num = int(d)
        total = total + num ** n
    return total == number