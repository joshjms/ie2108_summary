def reverse_nonrecursive(s):
    return s[::-1]

def reverse_recursive(s):
    if len(s) == 0:
        return s
    return reverse_recursive(s[1:]) + s[0]