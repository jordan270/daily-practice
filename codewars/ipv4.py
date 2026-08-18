def ips_between(start, end):
    start_part = start.split(".")
    end_part = end.split(".")
    
    start_total = 0
    for part in start_part:
        start_total = start_total * 256 + int(part)
        
    end_total = 0
    for part in end_part:
        end_total = end_total * 256 + int(part)
        
    return end_total - start_total