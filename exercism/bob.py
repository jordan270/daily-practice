def response(hey_bob):
    trimmed = hey_bob.strip()

    if trimmed == "":
        return "Fine. Be that way!"
    
    is_yelling = trimmed.isupper()
    is_question = trimmed.endswith("?")

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
        

        
