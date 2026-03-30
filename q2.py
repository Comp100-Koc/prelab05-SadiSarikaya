def remove_adjacent_duplicates(s):
    changed = True
    while changed:
        changed = False
        for i in range(len(s)):
            if i + 2 <= len(s) and s[i] == s[i+1]:
            
                s = s[:i] + s[i+2:]
                changed = True
            
            
    return s