def is_valid(isbn):
    
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False

    total = 0
    for i, ch in enumerate(isbn):
        if ch == "X" and i == 9:
            value = 10
        elif ch.isdigit():
            value = int(ch)
        else:
            return False
        total += value * (10 - i)
    if total % 11 == 0:
        return True
    else:
        return False
            
                
        
