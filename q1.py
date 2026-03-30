def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    temp = ""
    k= 0
    for i in range(len(s)-1,1,-1):
        for j in range(0,len(s)-2-k):
            if s[j:i+1] == s[j:i+1][::-1]:
                c = s[j:i+1]
                if max(len(temp),len(c)) == len(c):
                    temp = c
                
        k +=1
    if len(temp) <= 1:
        return ""
    
    return temp
            
