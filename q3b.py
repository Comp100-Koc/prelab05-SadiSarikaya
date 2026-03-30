def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    temp1 = a[2:]
    temp2 = b[2:]
    result1 = 0
    result2 = 0
    string = ""
    k = 0
    m = 0
    for i in range(len(temp1)-1,-1,-1):
        
        if int(temp1[i]) == 1:
            result1 += 2 ** k
        k+=1
    for j in range(len(temp2)-1,-1,-1):
        if int(temp2[j]) == 1:
            result2 += 2 ** m
        m+=1
        
    sum_result = result1 + result2
    
    print(sum_result)
    i = 0
    while 2 ** i <= sum_result:
        i += 1
    print(i)
        
    for j in range(i-1,-1,-1):
        if sum_result // 2 ** j >= 1:
            string += "1"
            sum_result -= 2 ** j
        else:
            string += "0"
            

        
    return "0b" + string
        
        

        
        
        
        
        