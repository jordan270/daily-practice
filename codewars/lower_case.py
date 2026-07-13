import re

def lowercase_count(strng):
    matches = re.findall(r"[a-z]", strng)
    return len(matches)