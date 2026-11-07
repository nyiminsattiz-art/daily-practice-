def average_string(s):
    digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    if not s or len(s.split()) == 0:
        return "n/a"
    
    s = s.split(" ")
    total = 0
    for i in s:
        if i not in digit:
            return "n/a"
        total += digit.index(i)
    avg =  total // len(s)
    return digit[avg]
