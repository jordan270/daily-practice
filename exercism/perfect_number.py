def classify(number):
    if number < 1:
        raise ValueError("Class")
    proper_divisors = []
    for i in range(1, number):
        if number % i == 0:
            proper_divisors.append(i)
            sum_of_divisors = sum(proper_divisors)
            if sum_of_divisors < number:
                return "deficient"
            elif sum_of_divisors == number:
                return "perfect"
            else:
                return "abundant"