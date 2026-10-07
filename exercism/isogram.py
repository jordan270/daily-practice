def is_isogram(phrase):
    seen = set()
    for char in phrase.lower():
        if char.isalpha():
            if char in seen:
                return False  # Duplicate found
            seen.add(char)
    return True