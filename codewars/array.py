def find_outlier(integers):
    evens = [i for i in integers if i % 2 == 0]
    odds = [i for i in integers if i % 2 != 0]
    
    # Whichever group has only 1 element is the "outlier" group
    return evens[0] if len(evens) == 1 else odds[0]