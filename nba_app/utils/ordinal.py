# Function to format ordinal numbers (1st, 2nd, 3rd)
def ordinal(n):
    if n == "Undrafted":
        return ""
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return str(n) + suffix