def main():
    number = int(input("enter the number of square (1-64): "))
    print(square(number))

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    grains = 1
    count = 1
    while count < number:
        grains = grains * 2
        count += 1
    return grains

def total():
    grains = 0
    square_grains = 1
    count = 0
    while count < 64:
        grains = grains + square_grains
        square_grains = square_grains * 2
        count += 1
    return grains

if __name__ == "__main__":
    main()